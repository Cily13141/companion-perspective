#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""伴侣视角原型 · Day 1 工具

三件事：
1. 生成 3 张示意图样例照片        -> assets/samples/*.png
2. 用 Pillow 实现参考版感官变换     -> assets/samples/reference/*.png
   （与 index.html 里的 JS 版数学完全一致，用作正确性参照与离线兜底）
3. 把 science.json 与样例照片内联进 index.html（file:// 下 fetch 会被拦截，
   且本地图片会污染 canvas，所以必须内联成 data URI）

可重复运行（幂等）。
"""
import base64
import io
import json
import math
import os
import re
import sys

import numpy as np
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SAMPLES = os.path.join(ROOT, "assets", "samples")
REFDIR = os.path.join(SAMPLES, "reference")
INDEX = os.path.join(ROOT, "index.html")
SCIENCE = os.path.join(ROOT, "science.json")

W, H = 1000, 667

# ---------------------------------------------------------------- 变换数学
# sRGB(线性) <-> LMS，Hunt-Pointer-Estevez 矩阵对（CIECAM97s 使用）
LMS_M = np.array([
    [0.38971, 0.68898, -0.07868],
    [-0.22981, 1.18340, 0.04641],
    [0.0, 0.0, 1.0],
], dtype=np.float64)
LMS_MI = np.array([
    [1.91020, -1.11212, 0.20191],
    [0.37095, 0.62905, 0.0],
    [0.0, 0.0, 1.0],
], dtype=np.float64)

# 物种参数（与 index.html 的 SPECIES 完全一致）
#   sat  : 降饱和程度
#   gain : 暗视觉亮度增益（勾选「昏暗环境」时生效）
#   lmix : 合并中/长波锥体时 M（绿）通道的权重——犬的保留锥体偏黄、猫偏蓝绿
#   tint : 线性 RGB 乘子，参数化表达上述光谱偏置（属示意性参数，非实测数据）
SPECIES = {
    "cat": {"sat": 0.65, "gain": 1.25, "lmix": 0.38, "tint": (0.96, 1.03, 1.05)},
    "dog": {"sat": 0.72, "gain": 1.05, "lmix": 0.50, "tint": (1.05, 1.00, 0.95)},
}


def srgb_to_linear(c):
    c = c / 255.0
    return np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)


def linear_to_srgb(c):
    c = np.clip(c, 0.0, 1.0)
    s = np.where(c <= 0.0031308, c * 12.92, 1.055 * (c ** (1 / 2.4)) - 0.055)
    return np.clip(np.round(s * 255.0), 0, 255).astype(np.uint8)


LUMA = np.array([0.2126, 0.7152, 0.0722])


def transform_array(rgb_u8, species="cat", dim=False):
    """rgb_u8: (h, w, 3) uint8 -> 变换后的 uint8。与 index.html 的 JS 版一致。

    关键设计：合并锥体通道会改变亮度（红会变暗），如果不校正，观众看到的是
    「变暗」而不是「色觉不同」。因此这里在降饱和前先把亮度校正回原始值——
    本模拟展示的是**色觉差异**，不是亮度感知差异，页面上对此有明确说明。
    """
    p = SPECIES[species]
    lin = srgb_to_linear(rgb_u8.astype(np.float64))          # (h,w,3)
    flat = lin.reshape(-1, 3)
    y0 = flat @ LUMA                                         # 原始相对亮度
    lms = flat @ LMS_M.T                                     # 到 LMS
    mix = p["lmix"]
    merged = lms[:, 0:1] * (1.0 - mix) + lms[:, 1:2] * mix    # 合并中/长波锥体
    lms[:, 0:1] = merged
    lms[:, 1:2] = merged
    back = lms @ LMS_MI.T                                    # 回线性 RGB
    y1 = back @ LUMA
    back = back * np.clip(y0 / np.maximum(y1, 1e-6), 0.4, 2.5)[:, None]
    back = back * np.array(p["tint"])                        # 物种光谱偏置
    y2 = back @ LUMA
    sc2 = np.clip(y0 / np.maximum(y2, 1e-6), 0.4, 2.5)
    back = back * sc2[:, None]
    lum = (y2 * sc2)[:, None]
    out = lum + (back - lum) * p["sat"]                      # 降饱和
    if dim:
        out = out * p["gain"]                                # 暗视觉亮度示意
    return linear_to_srgb(out).reshape(rgb_u8.shape)


def transform_viewpoint(img, species="cat"):
    """低视角示意：去掉上部、向下压，并轻微纵向拉伸（明确标注为示意）。"""
    w, h = img.size
    top = int(h * 0.18)
    bottom = int(h * 0.04)
    crop = img.crop((0, top, w, h - bottom)).resize((w, h), Image.LANCZOS)
    return crop


# ---------------------------------------------------------------- 样例绘制
def _bg(d, w, h, wall, floor_col, floor_ratio=0.34):
    d.rectangle([0, 0, w, h], fill=wall)
    fy = int(h * (1 - floor_ratio))
    d.rectangle([0, fy, w, h], fill=floor_col)
    # 地板拼缝
    for i in range(1, 9):
        x = int(w * i / 9)
        d.line([(x, fy), (x - 30, h)], fill=tuple(max(0, c - 18) for c in floor_col), width=2)
    d.line([(0, fy), (w, fy)], fill=tuple(max(0, c - 30) for c in floor_col), width=3)
    return fy


def _plant(d, x, y, s=1.0):
    pot_h = int(46 * s)
    d.polygon([(x - 26 * s, y), (x + 26 * s, y), (x + 19 * s, y + pot_h), (x - 19 * s, y + pot_h)],
              fill=(186, 118, 84))
    for ang, ln in ((-70, 70), (-45, 88), (-20, 76), (10, 84), (40, 66)):
        a = math.radians(ang)
        ex, ey = x + math.cos(a) * ln * s, y + math.sin(a) * ln * s
        d.line([(x, y - 6 * s), (ex, ey)], fill=(58, 122, 74), width=max(3, int(7 * s)))
        d.ellipse([ex - 17 * s, ey - 12 * s, ex + 17 * s, ey + 12 * s], fill=(74, 148, 88))


def _pendant(img, x, drop=120, shade=(244, 214, 148), glow=(255, 246, 214)):
    """吊灯（强光源）。光晕用半透明叠加，避免出现硬边同心圆靶心。"""
    d = ImageDraw.Draw(img)
    d.line([(x, 0), (x, drop)], fill=(130, 132, 136), width=5)
    d.polygon([(x - 50, drop), (x + 50, drop), (x + 36, drop + 56), (x - 36, drop + 56)], fill=shade)
    d.ellipse([x - 36, drop + 30, x + 36, drop + 80], fill=glow)
    ov = Image.new("RGBA", img.size, (0, 0, 0, 0))
    od = ImageDraw.Draw(ov)
    for r, a in ((130, 26), (215, 15), (300, 8)):
        od.ellipse([x - r, drop + 55 - r, x + r, drop + 55 + r], fill=tuple(glow) + (a,))
    img.paste(Image.alpha_composite(img.convert("RGBA"), ov).convert("RGB"), (0, 0))


def _lamp(d, x, y, shade=(242, 206, 138)):
    d.line([(x, y), (x, y - 150)], fill=(120, 122, 126), width=6)
    d.line([(x - 34, y), (x + 34, y)], fill=(120, 122, 126), width=6)
    d.polygon([(x - 46, y - 150), (x + 46, y - 150), (x + 32, y - 210), (x - 32, y - 210)], fill=shade)
    d.ellipse([x - 60, y - 172, x + 60, y - 128], fill=(255, 238, 190))


def _cat(d, x, y, s=1.0, body=(126, 130, 138), dark=(98, 102, 110)):
    """侧坐的猫。y 为地面线。"""
    x, y = float(x), float(y)
    # 尾巴（包围盒与身体重叠，确保连接）
    d.arc([x - 24 * s, y - 92 * s, x + 74 * s, y - 8 * s], 300, 62,
          fill=dark, width=max(3, int(9 * s)))
    # 身体
    d.ellipse([x - 52 * s, y - 70 * s, x + 40 * s, y - 6 * s], fill=body)
    # 前腿
    d.rectangle([x - 40 * s, y - 26 * s, x - 28 * s, y], fill=body)
    d.rectangle([x - 18 * s, y - 26 * s, x - 6 * s, y], fill=body)
    # 头
    d.ellipse([x - 66 * s, y - 104 * s, x - 8 * s, y - 46 * s], fill=body)
    # 耳
    d.polygon([(x - 62 * s, y - 96 * s), (x - 66 * s, y - 122 * s), (x - 42 * s, y - 100 * s)], fill=body)
    d.polygon([(x - 30 * s, y - 100 * s), (x - 14 * s, y - 122 * s), (x - 12 * s, y - 92 * s)], fill=body)
    # 眼与鼻
    d.ellipse([x - 54 * s, y - 84 * s, x - 46 * s, y - 76 * s], fill=(32, 34, 38))
    d.ellipse([x - 32 * s, y - 84 * s, x - 24 * s, y - 76 * s], fill=(32, 34, 38))
    d.polygon([(x - 44 * s, y - 70 * s), (x - 36 * s, y - 70 * s), (x - 40 * s, y - 63 * s)],
              fill=(214, 140, 140))


def sample_livingroom(path):
    """客厅：红沙发 / 绿植 / 蓝垫 —— 二色觉下红绿会「撞色」，蓝色保留。"""
    img = Image.new("RGB", (W, H), (232, 228, 220))
    d = ImageDraw.Draw(img)
    fy = _bg(d, W, H, (234, 230, 222), (196, 136, 86))
    # 窗户 + 光
    d.rectangle([70, 90, 330, 330], fill=(198, 220, 236))
    d.rectangle([70, 90, 330, 330], outline=(238, 240, 242), width=8)
    d.line([(200, 90), (200, 330)], fill=(238, 240, 242), width=6)
    d.line([(70, 210), (330, 210)], fill=(238, 240, 242), width=6)
    d.polygon([(330, 120), (620, fy + 60), (560, H), (330, 330)], fill=(246, 240, 226))
    # 红沙发
    d.rectangle([470, 330, 900, 470], fill=(198, 74, 66))
    d.rectangle([470, 300, 900, 345], fill=(214, 92, 82))
    d.rectangle([470, 430, 900, 500], fill=(168, 58, 52))
    d.rounded_rectangle([500, 312, 620, 400], 10, fill=(216, 104, 94))
    d.rounded_rectangle([640, 312, 760, 400], 10, fill=(216, 104, 94))
    # 蓝垫（二色觉下依然可分）
    d.rounded_rectangle([790, 320, 884, 396], 12, fill=(66, 104, 178))
    # 绿植
    _plant(d, 372, fy + 112, 0.95)
    # 吊灯（光源）
    _pendant(img, 650)
    # 猫 + 猫砂盆 + 猫爬架
    _cat(d, 505, H - 52, 1.0)
    d.rounded_rectangle([150, H - 96, 300, H - 26], 8, fill=(120, 132, 146))
    d.rectangle([160, H - 96, 290, H - 86], fill=(148, 160, 172))
    d.rectangle([930, 250, 986, fy + 70], fill=(178, 150, 116))
    d.rectangle([912, 250, 1000, 268], fill=(198, 172, 138))
    d.rectangle([912, 340, 1000, 356], fill=(198, 172, 138))
    img.save(path)


def sample_multicat(path):
    """多猫家庭：两个食盆挨在一起（应分离）、只有一个猫砂盆。"""
    img = Image.new("RGB", (W, H), (236, 232, 226))
    d = ImageDraw.Draw(img)
    fy = _bg(d, W, H, (238, 234, 228), (188, 148, 104))
    d.rectangle([60, 80, 300, 340], fill=(206, 214, 222))
    d.rectangle([60, 80, 300, 340], outline=(244, 246, 248), width=7)
    # 柜子
    d.rectangle([600, 120, 960, 380], fill=(176, 142, 108))
    d.rectangle([620, 150, 780, 250], outline=(150, 118, 88), width=5)
    d.rectangle([800, 150, 940, 250], outline=(150, 118, 88), width=5)
    # 红垫
    d.rounded_rectangle([330, fy + 30, 620, fy + 130], 14, fill=(192, 78, 68))
    # 两个紧挨的食盆 + 水盆挤在一起
    d.ellipse([352, fy + 140, 428, fy + 186], fill=(96, 150, 196))
    d.ellipse([366, fy + 148, 414, fy + 178], fill=(66, 104, 178))
    d.ellipse([436, fy + 140, 512, fy + 186], fill=(96, 150, 196))
    d.ellipse([450, fy + 148, 498, fy + 178], fill=(66, 104, 178))
    # 仅一个猫砂盆
    d.rounded_rectangle([700, H - 110, 900, H - 24], 10, fill=(126, 138, 152))
    d.rectangle([712, H - 104, 888, H - 86], fill=(154, 166, 178))
    _cat(d, 300, H - 52, 0.95)
    _cat(d, 430, fy + 118, 0.95, body=(148, 138, 128), dark=(120, 110, 100))
    _plant(d, 940, fy + 120, 0.85)
    img.save(path)


def sample_windowlamp(path):
    """强光源场景：用于闪烁融合频率说明。"""
    img = Image.new("RGB", (W, H), (226, 222, 216))
    d = ImageDraw.Draw(img)
    fy = _bg(d, W, H, (228, 224, 218), (176, 132, 92))
    # 大窗
    d.rectangle([80, 70, 430, 400], fill=(212, 232, 246))
    d.rectangle([80, 70, 430, 400], outline=(246, 248, 250), width=9)
    d.line([(255, 70), (255, 400)], fill=(246, 248, 250), width=7)
    d.line([(80, 235), (430, 235)], fill=(246, 248, 250), width=7)
    # 吊灯（强光源）
    _pendant(img, 700)
    # 桌子 + 红书 + 绿植
    d.rectangle([540, 430, 900, 452], fill=(168, 132, 96))
    d.rectangle([560, 452, 580, fy + 120], fill=(148, 114, 82))
    d.rectangle([860, 452, 880, fy + 120], fill=(148, 114, 82))
    d.rectangle([600, 396, 690, 430], fill=(190, 70, 62))
    d.rectangle([700, 402, 760, 430], fill=(178, 62, 56))
    _plant(d, 850, 400, 0.75)
    _cat(d, 330, H - 52, 1.0)
    d.rounded_rectangle([120, H - 104, 260, H - 30], 8, fill=(122, 134, 148))
    img.save(path)


# ---------------------------------------------------------------- 参考输出
def build_reference():
    os.makedirs(REFDIR, exist_ok=True)
    made = []
    for name in ("sample-livingroom", "sample-multicat", "sample-windowlamp"):
        src = os.path.join(SAMPLES, name + ".png")
        if not os.path.exists(src):
            print("  ! 缺少样例:", src)
            continue
        img = Image.open(src).convert("RGB")
        arr = np.asarray(img)
        panels = [arr,
                  transform_array(arr, "dog", False),
                  transform_array(arr, "cat", False)]
        gap = 14
        w, h = img.size
        strip = Image.new("RGB", (w * 3 + gap * 2, h), (255, 255, 255))
        for i, p in enumerate(panels):
            strip.paste(Image.fromarray(p), (i * (w + gap), 0))
        out = os.path.join(REFDIR, name + "-reference.png")
        strip.save(out)
        made.append(out)
    return made


def _dist(a, b):
    return float(np.sqrt(((a.astype(np.float64) - b.astype(np.float64)) ** 2).sum()))


def assert_deterministic():
    """自动断言：确定性 / 尺寸 / 值域 / 亮度保持 / 红绿混淆。"""
    img = Image.open(os.path.join(SAMPLES, "sample-livingroom.png")).convert("RGB")
    a = np.asarray(img)[:160, :160]
    r1 = transform_array(a, "cat", False)
    r2 = transform_array(a, "cat", False)
    assert np.array_equal(r1, r2), "变换不是确定性的"
    assert r1.shape == a.shape, "输出尺寸与输入不一致"
    assert r1.min() >= 0 and r1.max() <= 255, "输出超出 0-255 值域"

    # 亮度保持：本模拟展示的是「色觉差异」，不是「亮度差异」
    y0 = float((a.astype(np.float64) @ LUMA).mean())
    y1 = float((r1.astype(np.float64) @ LUMA).mean())
    rel = abs(y1 - y0) / max(y0, 1e-6)
    assert rel < 0.06, "亮度漂移过大: %.1f%%" % (rel * 100)

    # 红绿混淆：变换后红/绿之间的距离应显著小于原图
    red = np.zeros((1, 1, 3), np.uint8); red[0, 0] = (200, 40, 40)
    grn = np.zeros((1, 1, 3), np.uint8); grn[0, 0] = (40, 200, 40)
    before = _dist(red[0, 0], grn[0, 0])
    tr = transform_array(red, "dog", False)
    tg = transform_array(grn, "dog", False)
    after = _dist(tr[0, 0], tg[0, 0])
    assert after < before * 0.75, "红绿混淆未被模拟出来"

    # 犬/猫切换必须产生可见差异（对应验收标准「切换物种表现明显不同」）
    dc = transform_array(a, "dog", False).astype(np.float64)
    cc = transform_array(a, "cat", False).astype(np.float64)
    diff = float(np.abs(dc - cc).mean())
    assert diff > 1.5, "犬/猫切换的视觉差异过小: %.2f" % diff

    print("  断言通过：确定性 / 尺寸 / 值域")
    print("  亮度保持：原图平均亮度 %.1f → 变换后 %.1f（漂移 %.1f%%）" % (y0, y1, rel * 100))
    print("  红绿距离：原图 %.1f → 变换后 %.1f（缩小 %.0f%%）"
          % (before, after, (1 - after / before) * 100))
    print("  犬/猫输出平均通道差 %.2f（阈值 1.5）" % diff)


# ---------------------------------------------------------------- 内联进 HTML
def embed(index_path, science_path):
    html = open(index_path, encoding="utf-8").read()
    sci = open(science_path, encoding="utf-8").read().strip()
    json.loads(sci)  # 先验证是合法 JSON

    html = re.sub(
        r"(?s)(<script id=\"science-data\" type=\"application/json\">).*?(</script>)",
        lambda m: m.group(1) + sci + m.group(2),
        html,
        count=1,
    )

    items = []
    for sid, label in (("sample-livingroom", "客厅"),
                       ("sample-multicat", "多猫家庭"),
                       ("sample-windowlamp", "有窗有灯")):
        p = os.path.join(SAMPLES, sid + ".png")
        if not os.path.exists(p):
            continue
        b64 = base64.b64encode(open(p, "rb").read()).decode("ascii")
        items.append('{"id":"%s","label":"%s","src":"data:image/png;base64,%s"}'
                     % (sid, label, b64))
    samples_json = "[" + ",".join(items) + "]"

    html = re.sub(
        r"(?s)(<script id=\"sample-data\" type=\"application/json\">).*?(</script>)",
        lambda m: m.group(1) + samples_json + m.group(2),
        html,
        count=1,
    )
    open(index_path, "w", encoding="utf-8").write(html)
    return len(items), len(html.encode("utf-8"))


def main():
    os.makedirs(SAMPLES, exist_ok=True)
    print("[1/4] 生成样例照片")
    sample_livingroom(os.path.join(SAMPLES, "sample-livingroom.png"))
    sample_multicat(os.path.join(SAMPLES, "sample-multicat.png"))
    sample_windowlamp(os.path.join(SAMPLES, "sample-windowlamp.png"))
    for n in ("sample-livingroom", "sample-multicat", "sample-windowlamp"):
        p = os.path.join(SAMPLES, n + ".png")
        print("   %-22s %6.1f KB" % (n + ".png", os.path.getsize(p) / 1024))

    print("[2/4] 确定性断言")
    assert_deterministic()

    print("[3/4] 生成参考对比图")
    for p in build_reference():
        print("   %-40s %6.1f KB" % (os.path.basename(p), os.path.getsize(p) / 1024))

    print("[4/4] 内联进 index.html")
    n, size = embed(INDEX, SCIENCE)
    print("   内联 %d 张样例 + science.json -> index.html 共 %.1f KB" % (n, size / 1024))
    print("完成。")


if __name__ == "__main__":
    main()
