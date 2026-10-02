# 《伴侣视角》立项深度研究报告：用「宠物视角」帮饲主理解居家环境舒适度

**日期：** 2026-10-02
**Depth：** exhaustive（计划档位；实际检索量因并发限制低于档位上限，见「方法与限制」）
**Confidence：** 80%（第 2 轮补漏后由 74% 上调，见「方法与限制」）
**Sources：** 35 个来源；19 次 `web_fetch` 尝试（其中 11 次取得有效全文）；6 个 PDF 下载后本地提取；若干页面经本地下载＋正则抽取；1 次 Semantic Scholar 引文图谱查询
**研究对象：** Vibe Coding Camp · Team 2 立项《伴侣视角》——给猫狗饲主，在宠物日常生活环境中，理解／感知宠物视角，通过 VR 提供价值
**重心（按委托方指定）：** 科学依据 · 三天工程可行性 · 竞品与差异化

---

## 执行摘要 Executive Summary

**这个方向值得做，但「VR」和「代入宠物视角」这两件事必须拆开重新论证：前者是三天内最可能拖垮交付的约束，后者才是真正的差异化来源。** 需求侧证据是双重的：荷兰乌得勒支大学 2026 年发表于 PLOS ONE 的研究（n=647）证明，**养犬者识别宠物「细微疼痛信号」的能力并不优于非养犬者**，且系统性把「转头避开／僵住」误读为应激而非疼痛 [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)；英国 PDSA 与 YouGov 连续 14 年的全国代表性调查则给出同一结论结构的第二份证据——**95% 的猫主人自认已了解如何为猫提供合适环境，但 42% 的英国猫与另一只猫同住、近 180 万只猫可能因同居伙伴而应激** [PDSA PAW 2024](https://www.pdsa.org.uk/media/14944/pdsa_paw-report-2024.pdf)。而 2026 年初一款仅两人团队开发的「猫咪语言」App 一度登顶 iOS 付费榜，说明「想更懂宠物」已经产生真实付费行为 [新闻晨报/腾讯新闻](https://news.qq.com/rain/a/20260309A07U8S00)。机制侧同样有同行评议背书：东南大学 iStrayPaws 在 VRST 2024 证明**第一人称动物视角 VR 能显著提升状态共情与特质共情** [ACM VRST 2024](https://dl.acm.org/doi/10.1145/3641825.3687729)——但它也同时构成最直接的先行工作，对象是流浪动物而非家养宠物；**更紧迫的是，通过引文图谱可见 2025–2026 年已涌现一批「非人类具身 VR」作品（在 VR 中具身狗的耳朵、用鸟的感知做可穿戴、具身蜘蛛等），这条赛道正在被快速填充，而不只是一篇论文。**最大的可行性风险来自一条硬事实：**WebXR 在 iOS Safari 上至今不受支持**（caniuse 实测：Safari on iOS 3.2–27.2 全版本 Not supported）[caniuse](https://caniuse.com/webxr)，而中国宠主中 00 后占 26.3%、90 后占 42.7% [央视网/派读白皮书](https://business.cctv.com/2026/01/05/ARTIdmv2AWmVeRVodaZYLOvQ260105.shtml)，主力设备是手机而非头显。**最重要的一条保留意见：** 目前没有任何一项研究直接测量过「让饲主以宠物视角观察自己的家」是否真能提升其后续的环境改善行为——这是本报告置信度最低的环节（58%），也是三天 demo 最该去补的空白。

---

## 关键发现 Key Findings

1. **需求被同行评议量化了，而且比团队假设的更尖锐。** 问题不是「饲主不想懂」，而是「饲主以为自己懂、实际读不准细微信号」——PLOS ONE 2026 的 n=647 研究证实养犬者对细微疼痛信号识别率与非养犬者**无显著差异**，而对明显信号（如抬腿）识别率达 90% [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)。

2. **英国的全国代表性调查给出了同一个结论结构的第二份独立证据，而且数字更刺眼。** PDSA PAW 2024（与 YouGov 合作、连续 14 年的全国代表性调查）显示：**95% 的猫主人自认「已了解如何为猫提供合适的环境」，但现实中 42% 的英国宠物猫与另一只猫同住，其中 17%（约合 180 万只猫）与「并不总能相处」的猫同住**；多猫家庭的猫出现至少一种可能提示应激的行为的比例为 **55%**，独居猫为 **48%**，与相处不来的猫同住者高达 **67%** [PDSA PAW 2024](https://www.pdsa.org.uk/media/14944/pdsa_paw-report-2024.pdf)。

3. **「更懂宠物」已经被验证有人愿意付钱。** 2026 年初「猫咪语言」App 一度登顶 iOS App Store 付费榜榜首，开发团队仅两人；同类猫语翻译 App 订阅价 12 元/月与 68 元/月 [新闻晨报/腾讯新闻](https://news.qq.com/rain/a/20260309A07U8S00)。

4. **但最热的那条解法（声音翻译）已被专业行为咨询师公开否定。** 拥有十年、超 3000 例猫行为矫正经验的咨询师孙文指出：猫咪紧张焦虑的发声与发情／回应主人的声音**十分相似**，标准化翻译「极易造成南辕北辙的危险误判」；「人语转猫语」可能让猫产生困惑、紧张甚至应激并攻击主人 [同上](https://news.qq.com/rain/a/20260309A07U8S00)。

5. **专业兽医指南给出了「环境舒适度」的可操作定义，可信度远高于感官模拟。** AAFP 2021 猫科老年照护指南明确以「健康猫科环境的五大支柱」为框架，并把关键资源具化为**猫砂盆、食盆、饮水、睡窝、抓挠面、躲藏空间、三维立体空间，且需多处分布** [JFMS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10812122/)。

6. **饲主「意识不到渐变」是兽医临床的公认痛点，且专业人士认为饲主可被训练。** 同一指南写道「许多客户在未被问到引导性问题前，可能并未意识到逐渐发生的变化」，但同时指出「在适当指导下，客户能学会识别猫正常活动与行为模式中提示疼痛的改变」[同上](https://pmc.ncbi.nlm.nih.gov/articles/PMC10812122/)。

7. **「第一人称动物视角」的机制已被同行评议验证有效，但同时已被占位。** iStrayPaws（VRST 2024，东南大学）用第一人称 VR 呈现流浪动物的困境，用户研究显示 VRPT 组在状态共情与特质共情上均较传统方法显著提升 [ACM](https://dl.acm.org/doi/10.1145/3641825.3687729)。

8. **更紧迫的是：「非人类具身 VR」在 2025–2026 已经从单篇论文变成一个活跃研究前沿，赛道正在被快速填满。** 通过 Semantic Scholar 引文图谱追溯 iStrayPaws 的施引文献，可见同期一批直接相关的作品：**《Having Dog Ears "for Real"：Effects of Active and Passive Haptics on Embodying Non-Human Body Parts in VR》**（2026, arXiv）、**《Seeing with a Bird's Perception：Designing a Wearable Experience to Reorient Attention to Everyday Nature》**（CHI EA 2026）、**《Investigating How to Control Virtual Spiders While Embodying Them in Virtual Reality》**（VRST 2025）、**《Me, the Elephant, and the Virtual World》**（PACM HCI 2025）、**《ZooWear：Animal-Inspired Head-Mounted Haptic Interfaces》**（2025）等 [Semantic Scholar 引文图谱](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3641825.3687729/citations)。这意味着「动物视角／非人类具身」不再是无人区，**立项的时间窗口比团队预想的窄**。

9. **「宠物视角」在商业上已有轻度先例，但只做到「贴地拍摄」，没做到「感官模拟」。** Enabot 宠物陪伴机器人以贴地视角拍摄，用户把这种镜头视角称为「老鼠视角」，在短视频平台非常受欢迎；该公司全球用户已突破 100 万、覆盖 160 多国 [人民网/人民日报海外版](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)。

10. **三天内 VR 头显路线的最大障碍是浏览器支持，而不是美术工作量。** caniuse 显示 WebXR Device API 在 **Safari on iOS 全版本为 Not supported**（3.2–27.2），桌面 Safari 13–27 为「默认禁用」；Chrome 79–154 为「部分支持」[caniuse](https://caniuse.com/webxr)。

11. **头显的性能门槛有明确量化标准，且「掉帧」比「平均帧率低」更致命。** VR 的运动到光子延迟通常为 20–30 ms，90 fps 约合每帧 11 ms，已是 Quest 3／PSVR2 的基线；降到 72 fps 就足以在长时间使用中诱发不适 [LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps)。

12. **宠物的感官世界与人类差异巨大，这既是内容素材也是拟人化风险源。** 犬为二色视觉（蓝紫＋红，无法区分绿色）；猫总视野约 200°（其中双眼视野 140°）；人类引发视觉所需的阈值光强约为猫的 6 倍；犬猫锥细胞闪烁融合频率为 70–80 Hz，而人类约 60 Hz——**也就是说，人眼看着稳定不闪的灯，宠物可能看着在闪** [VetScienceWeek](http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf)。

13. **听觉差异是可以直接做进产品的最强「视角落差」证据。** 一项 2023 年综述整理的听阈数据：人类 31 Hz–8 kHz，犬 67 Hz–45 kHz，猫 58 Hz–75 kHz [Laboratory Animal Research](https://link.springer.com/article/10.1186/s42826-023-00182-3/tables/2)。

14. **拟人化在动物行为学界是真实争议，不是可以忽略的学术洁癖。** Burghardt 提出的「批判性拟人化」（critical anthropomorphism, 1991）至今仍被讨论，Nature 曾刊文《拟人化的危险》警告其回潮 [Anthropomorphism Revisited](https://comparative-cognition-and-behavior-reviews.org/wp/wp-content/uploads/2013/10/vol_2_commentary_timberlake.pdf)。

15. **中国宠物市场足够大但「理解宠物」尚不是消费类目。** 2025 年城镇犬猫消费市场 3126 亿元（+4.1%），但消费结构为食品 53.7%、医疗 27.6%、用品 12.2%、服务 6.5%，没有「理解／共情」这一项 [央视网](https://business.cctv.com/2026/01/05/ARTIdmv2AWmVeRVodaZYLOvQ260105.shtml)。

16. **行业内已明确把「理解宠物」当作下一代方向。** 索未来科技集团董事长刘聪凯公开表示，「未来宠物智能产品还将融入跨物种'语言'翻译功能……帮助人类更好理解宠物的'语言'」[人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)。

---

## 详细分析 Detailed Analysis

### 子问题 1：需求真实性——饲主「看不懂宠物」的痛点有多普遍、多强？

**结论：痛点真实、被量化，而且痛点结构对「视觉化理解」比对「声音翻译」更友好。**

这个问题在本项目里的价值，不在于证明「宠物市场很大」——那是显然的，2025 年城镇犬猫消费已达 3126 亿元、单只犬年均消费 3006 元 [央视网](https://business.cctv.com/2026/01/05/ARTIdmv2AWmVeRVodaZYLOvQ260105.shtml)——而在于证明**痛点存在且形式是「认知盲区」而非「缺乏工具」**。

PLOS ONE 2026 那项研究的设计恰好能回答这一点。研究者向 647 名参与者（530 名养犬者、117 名非养犬者）出示十七个犬类行为信号与三个犬只行为案例，请其评估「该行为与疼痛相关的可能性」。结果是**第一个假设被证实：养犬者识别细微疼痛信号的能力并不优于非养犬者**。对明显信号（与运动能力相关的疼痛，如持续抬起后腿）几乎所有参与者都能识别——620 个疼痛归因中有 555 个（90%）；但对**细微信号**案例（如黏人跟随家人、夜间躁动），养犬者与非养犬者之间**没有显著差异** [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)。

研究者的解释直指产品机会：「这可能表明养犬者识别细微疼痛信号时更不容易。养犬者可能更多把'转头或转身避开'与'僵住'识别为应激／恐惧信号，而不是疼痛信号。」更关键的是第二个发现：**有过疼痛经历的饲主识别率显著更高**（647 人中 363 人报告曾有个人疼痛经历），而**养过患病犬只的饲主**对细微信号的评分也显著更高——研究者据此认为「经验很重要」，并引用既有研究指出「一项针对若干疼痛信号的教育干预（使用改编的兽医犬疼痛工具）提升了养犬者解读可能提示疼痛的行为的能力」[同上](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)。

**这两点合起来，正好是本项目最有力的立项论据：** 饲主的短板是**经验缺口**，而不是态度问题；既然「经验」能补上这个缺口，那么**用技术手段人工制造经验**（让人体验一次宠物的感官与处境）在逻辑上是成立的干预路径。这与 iStrayPaws 把「共情」当作可干预变量的思路完全一致（见子问题 3）。

**英国的数据用另一条路径得到了同一个结论结构，而且更加反讽。** PDSA 与 YouGov 合作、已连续 14 年的全国代表性调查（PAW Report 2024，方法论已发表于同行评议期刊 *Veterinary Record*）给出了两组并列的数字：**95% 的猫主人自认「已了解如何为猫提供合适的环境」**——而同一份报告显示，**42% 的英国宠物猫与另一只猫同住**（其中 25% 与相处得来的猫同住、17% 与「并不总能相处」的猫同住，约合 **180 万只猫可能因同居伙伴而处于应激状态**）；出现至少一种可能提示应激的行为的比例，多猫家庭的猫为 **55%**、与相处不来的猫同住者为 **67%**、独居猫为 **48%**。报告列出的应激提示行为包括：对人或其他同住猫咆哮／拍打／咬、在猫砂盆外排泄、胆怯／恐惧／紧张、过度理毛、攻击不与其同住的猫、抓挠家具或门框地毯等。报告还指出，**把一只新猫引入家庭，对原本已在家的猫可能比对新猫更有压力** [PDSA PAW 2024](https://www.pdsa.org.uk/media/14944/pdsa_paw-report-2024.pdf)。

**把两组数据并排看，本项目的痛点定义就非常清楚了：「自认懂」与「实际做」之间存在系统性缺口，而且这个缺口在荷兰（疼痛信号识别）与英国（环境资源配置）用完全不同的方法各自被测量到了。** 这是我在本次检索中找到的、对「是否需要这个产品」最有力的双重证据。它也顺带给出了内容优先级：多猫家庭的资源分离（每只猫独立的食盆、水盆、猫砂盆、睡窝、躲藏处）是**证据最强、最容易可视化、也最容易被饲主忽略**的一项——因为 95% 的人认为自己已经做到了。

**但在付费意愿这一环，我必须指出证据的性质差异。** 我找到的最强证据是媒体报道而非调研数据：2026 年初「猫咪语言」App 一度登顶 iOS 付费榜，同类产品订阅价 12 元/月至 68 元/月，商业模式普遍为「先免费试用、后自动续费」[新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。**登顶付费榜是真实付费行为，这很有说服力；但它同时也说明一个残酷事实：付费的是「音频 App」，成本结构几乎为零（两人团队、素材部分来自自家猫），而不是「沉浸式 VR 内容」。** 用前者的付费数据去支撑后者的制作成本，是不成立的。中国本土也**没有**找到任何一份量化「饲主读不懂宠物」比例的调研——现有最强证据来自荷兰（PLOS ONE）与英国（PDSA），跨文化效度未经检验。

> 「广大铲屎官渴望与宠物进行『交流』的强烈需求」——[新闻晨报对猫语翻译 App 热潮的报道](https://news.qq.com/rain/a/20260309A07U8S00)

**跨子问题关联**：本子问题确认了痛点的**心理结构**（自认懂、实际读不准），这直接决定了子问题 2 的科学边界——能补上「经验缺口」的是**可验证的感官／行为事实**，而不是拟人化的情绪叙事（见子问题 2 与「矛盾与分歧」）。

---

### 子问题 2：科学依据——猫狗感官与「环境舒适度」中，哪些有据可依、哪些是拟人化过度？

**结论：感官差异部分是硬科学，可以放心作为内容骨架；「环境舒适度」有权威专业框架可以依附；但「代入宠物视角」这个说法本身踩在拟人化争议上，必须用措辞和呈现方式主动规避。**

先把可信的部分钉死。**视觉**方面，一份兽医继续教育论文给出的结论是：犬为二色视觉，锥细胞分别吸收蓝紫与红光谱，**因此犬能看见颜色，但无法区分绿色**；猫的总视野估计为 200°，其中中央双眼视野 140°，两侧单眼视野各 30°；猫因角膜与瞳孔大、且有照膜（tapetum lucidum）反光，**引发视觉所需的阈值光强，人类约为猫的 6 倍**；但照膜也导致**视觉锐度下降**，因为被反射的光子在眼内散射 [VetScienceWeek](http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf)。

还有一个非常适合做「视角落差」演示的细节：**锥细胞闪烁融合频率在人类约为 60 Hz，而动物为 70–80 Hz**。这意味着人类看着连续不闪的光源，宠物可能感知为闪烁——该文甚至据此建议兽医诊室「使用不闪烁的灯泡对患畜视觉更友好」[同上](http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf)。这是一个**能被三天 demo 直接视觉化、且反直觉**的知识点，价值极高。

**听觉**同样有干净的数据。2023 年一篇综述整理的听阈表（60 dB SPL 下）：人类 31 Hz–8 kHz（最敏感 −10 dB SPL @ 2–4 kHz），犬 67 Hz–45 kHz（最敏感 0 dB SPL @ 2–8 kHz），猫 58 Hz–75 kHz（最敏感 −3 dB SPL @ 8–16 kHz），数据分别引自 Heffner 等人的经典听力学研究 [Laboratory Animal Research](https://link.springer.com/article/10.1186/s42826-023-00182-3/tables/2)。

**嗅觉这一环需要打折扣引用。** 我最终只找到一份大学课程讲义（伊利诺伊大学 ANSC 207《Special Senses》）给出了具体对比：嗅上皮面积**犬 18–150 cm²、人类 3–4 cm²**，嗅觉受体数量**犬 >1.5 亿、人类 500 万** [University of Illinois CITL](https://cdn.citl.illinois.edu/courses/ansc207/week2/special_senses/web_data/file10.htm)。⚠️ **这是 Tier 3 教学材料，未标注一次文献，且这两个数字在文献中口径差异很大**（受体数常见说法从 1.25 亿到 3 亿皆有）。因此我在报告中**只把它当作量级参考**：犬的嗅上皮面积与受体数量比人类高一到两个数量级——这个方向性结论是稳健的，具体数值不可依赖。值得注意的是，与视觉、听觉不同，**嗅觉差异在现有 VR 技术下几乎无法被真实模拟**（没有消费级嗅觉显示器），这反而说明：产品若要做嗅觉，只能用叙事与画面暗示，而不是还原——这正好是拟人化风险最高、也最容易被专业方质疑的地方。

**「环境舒适度」这一侧，专业界并没有用「感官模拟」来定义它，而是用「资源」。** AAFP 2021 猫科老年照护指南以「健康猫科环境的五大支柱」为框架（原文明确引用该框架），并把「关键资源」具化为：**猫砂盆、食盆、饮用水、睡窝、抓挠面、躲藏空间，以及三维立体空间，且需分布在住宅内的多个位置**；指南还建议为老年猫提供夜灯、坡道与台阶以便接近喜爱的高处 [JFMS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10812122/)。该框架的原始出处是 2013 年 AAFP/ISFM 猫科环境需求指南（Ellis、Rodan 等，发表于 *Journal of Feline Medicine and Surgery*），其五大支柱的官方表述为：**一个安全的地方；多个且相互分离的关键环境资源；玩耍与捕猎行为的机会；积极、一致且可预测的人猫社交互动；以及尊重猫的嗅觉重要性的环境** [EurekAlert 新闻稿](https://www.eurekalert.org/news-releases/511468)。

> 「就像我们对猫的医疗决策所做的那样，我们为猫提供的环境所做的决定，必须基于坚实证据基础所产生的信息。」——指南共同主席 Sarah Ellis 博士 [EurekAlert](https://www.eurekalert.org/news-releases/511468)

**这对产品定义是一个决定性的提醒：** 「居家环境舒适度」在专业上不是一种「感受」，而是一张**可核查的资源清单**（几个猫砂盆、放在哪、有没有躲藏处、有没有垂直空间）。这意味着项目如果要做「感知环境舒适度」，最容易被专业方认可的形态不是「让饲主感受猫的情绪」，而是**让饲主以猫的身体尺度与感官重新「看见」自己的家，并对照五大支柱发现资源缺口**。这恰好也是三天内能做出可演示效果的东西——把「资源缺口」可视化，比模拟情绪可靠得多，也更容易验证。

**拟人化风险必须正视。** 动物行为学界的争论由来已久：Burghardt 1991 年提出的「批判性拟人化」至今仍被作为需要辩护的概念讨论，Nature 曾以《拟人化的危险》为题警告拟人化的回潮，评论者直接追问「为什么拟人化仍然不是一种科学方法」[Anthropomorphism Revisited](https://comparative-cognition-and-behavior-reviews.org/wp/wp-content/uploads/2013/10/vol_2_commentary_timberlake.pdf)。本项目的风险不在于用了拟人化，而在于**把拟人化的结果当作关于动物的事实来宣称**。可行的规避方式是措辞纪律：宣称「我们可视化猫的视野／听阈／身体尺度」（可证伪），而不要宣称「我们知道猫此刻在想什么」（不可证伪）。

**跨子问题关联**：本子问题为子问题 3 的差异化定位提供了依据——竞品（猫语翻译 App）恰恰踩在最不可靠的那一侧（把发声翻译为人类语言），而本项目可以站在最可靠的那一侧（可视化的感官与资源事实）。这也是下面「矛盾与分歧」中专家批评的技术根源。

---

### 子问题 3：竞品与差异化——谁做过、做到什么程度、空位在哪？

**结论：机制有学术占位者，视角有轻度商业先例，但「家养宠物 + 饲主侧 + 自家居家环境」这个具体组合仍是空位；而最大的竞品不是硬件，是「声音翻译」这条被专家否定的捷径。**

先看最近的先行工作。**iStrayPaws**（东南大学，VRST 2024，DOI 10.1145/3641825.3687729）是本报告找到的最直接对标：它指出 VRPT（Virtual Reality Perspective-Taking）虽在共情诱导上有效，但应用「主要集中于弱势人类，而非动物」，而既有的动物相关工作「主要针对农场动物与野生动物」；该系统让用户以第一人称经历流浪动物遭遇的恶劣天气、饥饿与疾病，并加入视听与动觉设计；用户研究显示 **VRPT 受试者在状态共情与特质共情上均较传统方法有显著提升** [ACM VRST 2024 / 摘要](https://dl.acm.org/doi/10.1145/3641825.3687729)。

这是一个双向结论。**正面**：机制有效，且是被同行评议验证过的，团队方向不是空中楼阁。**负面**：机制本身不再新颖，「第一人称动物视角 VR」的学术占位已被拿下，而且是在一个学术会议上。团队如果以「首创宠物视角 VR」作为立项话术，是经不起追问的。真正可辩护的差异在于**对象与目标**：iStrayPaws 是**流浪动物 + 苦难叙事 + 同情**，本项目是**家养宠物 + 居家环境 + 理解**——用户不同（潜在领养者 vs 已有饲主）、情感目标不同（同情 vs 理解）、场景不同（街头 vs 自家客厅）。后者恰恰落在 iStrayPaws 自己划定的范围之外：其摘要明确把既有动物相关研究概括为「主要针对农场动物与野生动物」，并把自身定位为面向流浪动物的补位之作——**换言之，「家养宠物 + 饲主自己的居住环境」被它的定位排除在外**。

**而且这个赛道正在快速变窄，这是本次补漏中最值得警惕的发现。** 我通过 Semantic Scholar 的引文图谱追溯了 iStrayPaws 的施引文献，发现 2025–2026 年已经出现一批直接围绕「非人类具身」的作品，而不是零星一篇：**《Having Dog Ears "for Real"：Effects of Active and Passive Haptics on Embodying Non-Human Body Parts in VR》**（2026，arXiv）直接研究在 VR 中具身**狗的耳朵**；**《Seeing with a Bird's Perception：Designing a Wearable Experience to Reorient Attention to Everyday Nature》**（CHI EA 2026）做的是**鸟类感知的可穿戴体验**，把「用别的物种的感官看日常环境」这一核心创意搬进了真实产品形态；此外还有《Investigating How to Control Virtual Spiders While Embodying Them in Virtual Reality》（VRST 2025）、《Me, the Elephant, and the Virtual World》（PACM HCI 2025）、《ZooWear：Animal-Inspired Head-Mounted Haptic Interfaces》（2025）等 [Semantic Scholar 引文图谱](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3641825.3687729/citations)。一篇 2025 年发表的沉浸式共情计算系统性综述（覆盖 2000–2024 年文献）也已经把「VR 跨越物种共情」写进结论，并以 iStrayPaws 作为该方向的代表案例，称其通过 VRPT 系统「促进对流浪动物的共情并推动动物福利的意识与行为改变」[Empathic Computing 综述](https://oss.sciexplor.com/manuscript/329/publish/EC-202501.pdf)。

**这一发现改变了差异化论证的性质。** 原先是「机制被占位、但邻域空旷」，现在是「**机制被占位、且邻域正在被快速填充**」——尤其《Seeing with a Bird's Perception》几乎就是同一命题（用他物种感官重新注意日常环境）在鸟类与自然连接场景下的实现。这意味着本项目的窗口不是「有没有人做」，而是「**在什么时候、由谁把家养宠物的居家环境这一格补上**」。对三天立项的直接含义是：不能只讲创意，必须把「为什么是我们、为什么是这个物种、为什么是这个场景」讲清楚。

**商业侧的先例比想象中近，但也比想象中浅。** Enabot（赋之科技）的宠物陪伴机器人以贴地视角拍摄，其市场负责人明确说「陪伴机器人的贴地视角就很好地解决了这个问题（拍不到小猫喝水角度）」，并且**用户把这种镜头视角称为「老鼠视角」，在互联网上非常受欢迎，也符合短视频平台的传播特征**；该公司全球用户已突破 100 万、覆盖 160 多个国家，海外营收占六成 [人民网/人民日报海外版](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)。**这段证词的价值在于：它证明了「非人类视角的内容」本身有传播力和用户接受度，而且已经被商业化验证——但它只做到「把相机放低」，没有做到「用猫的感官和身体尺度重建世界」。** 这正是本项目的空位：从「换个机位」升级为「换个物种的感知系统」。

**但真正需要警惕的竞品是「声音翻译」，因为它更快、更便宜、更接近用户的语言。** 2026 年初「猫咪语言」App 一度登顶 iOS 付费榜（两人团队），同类 App 大量涌现，提供人猫语言双向互译，还有微信小程序与实体「宠物翻译器」硬件；MeowTalk（喵语）称其用兽医科研中收集标注的猫发声数据训练专有 AI 模型；订阅价从 12 元/月到 68 元/月不等 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。

**而这条捷径有硬伤，且已被专业人士公开点破。** 猫行为咨询师孙文（十年、超 3000 例猫行为问题矫正经验）的判断是：把猫叫标准化翻译「不够准确且片面」；猫对人的发声大部分是幼猫与母猫沟通方式的延续，具体需求多样化，「不同的猫面对不同的人发音方式也可能会有不同，因为无法简单地把猫表达需求的发声翻译成『我饿了』这样的人类语言」；**最危险的是「猫咪紧张焦虑时的负面情绪发声，与发情或回应主人的声音十分相似，如果按照软件的标准化翻译，极易造成南辕北辙的危险误判」**；「人语转猫语」功能更是不可取，因为猫与人之间并不依靠猫叫声交流，电子合成声可能被猫误认为陌生同类，若碰巧代表负面情绪，「很容易导致猫咪产生困惑、紧张甚至严重的应激反应，进而引发对主人的攻击」[新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。

> 「只有将声音与肢体动作结合起来，才能真正当好宠物的『贴身翻译官』。」——猫行为咨询师孙文，建议饲主观察「放松的坐姿、翘起的尾巴和细小的瞳孔」与「夹着尾巴、耳朵后压、弓背炸毛或面部紧绷」的差别 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)

**这段话几乎是为本项目写的定位说明：** 行业最热的产品线（声音翻译）被专业方判定为不可靠甚至有害，而专业方给出的正确路径是**多模态的、以肢体与情境为主的观察**——这正是「视觉／情境化理解」的主场，也正是「宠物视角」能提供而「声音翻译」提供不了的东西。同时它也是一个警告：**如果本项目为了三天 demo 的传播效果而加入「翻译猫在说什么」的功能，就会主动跳进这个已经被专业方否定的坑里。**

其他竞品形态相对边缘：GoPro Fetch 犬用胸背带属于「第一视角拍摄」的硬件方案（厂商页面可见）[GoPro](https://gopro.com/es/pe/shop/mounts-accessories/fetch-dog-harness/ADOGM-001.html)；室内宠物摄像头是一个稳定增长但拥挤的品类（中文市场研究报告给出约 8.5% CAGR 的口径，属 Tier 3-4，仅供参考）[格隆汇](https://dxpress.gelonghui.com/p/3266208)。中国市场的智能宠物品类集中在喂食器、饮水机、猫砂盆、智能舱与陪伴机器人，宠主一次购置可达 2000 元以上 [人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)——**注意这些产品全部在做「宠物侧的数据与照料」，没有一个是做「饲主侧的感知与理解」。**

**跨子问题关联**：本子问题的空位判断依赖子问题 2 的科学边界——空位之所以存在，部分原因是它要求制作方掌握饲主通常不具备的感官与行为学知识。**但第 2 轮的引文图谱显示这道「护栏」正在变薄**：2025–2026 年已有多组研究者分别切入「他物种感官」这一命题（狗耳朵、鸟的感知、蜘蛛具身），说明门槛并不像原先估计的那样高。因此差异化的可持续性更多取决于**场景与数据的独占性**（家养宠物 + 饲主自家环境 + 依附权威资源清单），而不是知识门槛本身；可行性则仍依赖子问题 4 的技术路线选择。

---

### 子问题 4：三天工程可行性——什么能做出来，什么做不出来？

**结论：如果坚持「头显 VR」，三天内最可能交付的是一段不能给现场观众试戴的视频；如果接受降级，三天内可以做出一个真正可交互、可在手机上打开的第一人称「猫的身体尺度」体验。技术路线的选择，是本次立项最大的单点决策。**

先看那条最硬的约束。**WebXR Device API 在 Safari on iOS 上从 3.2 到 27.2 全版本为「Not supported」；桌面 Safari 13 到 27 为「Disabled by default」；Chrome 79–154 为「Partial support」** [caniuse](https://caniuse.com/webxr)。这条结论经第二个独立 Tier 1 来源交叉验证：MDN 把 WebXR Device API 标注为「**Limited availability**」，并明确写道「**This feature is not Baseline because it does not work in some of the most widely-used browsers**」（该特性尚不属基线，因为它在若干最广泛使用的浏览器中无法工作），同时标记为实验性技术，建议生产环境谨慎使用 [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API)。（我另外查阅了 **Safari 27 的官方版本说明**，其中**未出现 WebXR 相关条目**，但这张页面体积很小、可能由脚本渲染，因此只作为弱旁证，不作为结论依据 [Apple Developer](https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes)。）这条事实的杀伤力在于它同时击中了两个要害：**（1）** 如果做网页端 WebXR，iPhone 用户（在中国是绝对主力）根本无法进入沉浸模式；**（2）** 如果改用原生 Unity／Unreal，则三天内不可能完成开发＋分发，而且**现场还得有头显**。换句话说，团队在立项表里把「VR」写成唯一机制，实际上是把交付押在了一个「既要求用户有头显、又要求用户不是 iPhone」的交集上——而这个交集非常小。

**头显的性能门槛也远比想象中严厉。** 一份 2026 年 3 月的工程实践总结指出：VR 的运动到光子延迟通常为 20–30 ms，**90 fps 约合每帧 11 ms，已是当代头显（Meta Quest 3、PlayStation VR2）的基线期待**；掉到 72 fps「就足以在长时间会话中触发不适」；一份 90 fps 的帧预算大致是 CPU 约 5 ms、GPU 约 5 ms、系统开销约 1 ms [LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps)。**三天内要在一个没做过 VR 的团队手里稳定跑满 90 fps 的 360° 场景，本身就是高风险项**——这也解释了为什么团队自己的打分矩阵里，候选 A 在「三天能否完成」这一维度只拿到 2/2/3（候选 B 是 5/5/5）。

**现实的降级路线，而且已经有现成零件可用。** 一条 360° 全景视频／图片路线可以在普通手机浏览器里跑：**@cloudimage/360-video** 是一个基于 Three.js 的交互式 360° 视频播放器，Akamai 也提供 A-Frame 的 AMP 360 播放器组件 [cloudimage-360-video](https://scaleflex.github.io/cloudimage-360-video/) [Akamai AMP A-Frame](http://mdtp-a.akamaihd.net/docs/web/amp-web-aframe/akamai.amp.aframe.AframeConfig.html)。这意味着「第一人称看一个空间」在**不依赖 WebXR、不依赖头显**的前提下是可实现的（触摸拖拽／陀螺仪视差），代价是沉浸感显著下降，收益是**任何人扫个二维码就能看**。此外，360° 消费级设备的门槛也不高：Insta360 X5 于 2025 年 4 月 22 日发布，与 X4 同样支持 8K/30fps，X5 采用 1/1.28 英寸双传感器、弱光表现明显提升，X4 在 5.7K/30fps 下实验室续航 135 分钟、X5 在 5.7K/24fps 下可达 185 分钟 [Trusted Reviews](https://www.trustedreviews.com/versus/insta360-x5-vs-x4)——**但更重要的一个问题是：把 360 相机放在离地 20 厘米的高度、在室内弱光下、追着一只不配合的猫拍摄，是一个独立的内容制作难题，而且它几乎不可能在三天内与开发并行完成。**

因此三天路线可以这样切分：**方案甲（推荐）**：放弃实时 3D，做「预渲染 360° 或伪 3D 视差 + 少量可交互热点」的网页体验，重心放在**视角差异的可视化对比**（例如同一客厅在「人眼 1.7 m 高度 + 三色视觉」与「猫眼 0.25 m 高度 + 二色视觉 + 高频闪烁可见」两种呈现下切换）；**方案乙（备选）**：完全放弃沉浸，做一张「猫的身体尺度 + 感官滤镜」的图像／短视频生成器，用户上传自己家的照片即可得到「猫眼中的样子」。方案乙的工程风险最低，而且**它天然回答了「三天结束演示什么」这个立项表上的空白**。

**跨子问题关联**：本子问题的结论会反向改写子问题 3 的差异化表述——如果最终交付的是「预渲染 360/伪 3D」，那么差异化就不能再建立在「VR 沉浸」上，而必须建立在「感官差异的准确性与可核查性」上，这与子问题 2 的结论完全一致。

---

### 子问题 5：效果验证——怎么证明「看过之后饲主真的更理解宠物」？

**结论：这是全报告证据最薄的一环。可以借用成熟的共情／观点采择量表与前后测设计，但「以宠物视角观察自己的家 → 饲主行为改变」这条因果链，目前没有任何直接研究支持。**

先说可借用的部分。iStrayPaws 的用户研究已经示范了这类干预的标准做法：以**状态共情与特质共情**作为结果变量，与「传统方法」做对照，并报告显著提升 [ACM](https://dl.acm.org/doi/10.1145/3641825.3687729)。在心理健康领域，一项基于心智化的 VR 团体干预随机对照试验直接使用**人际反应指针（IRI, Interpersonal Reactivity Index）**作为测量工具 [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2949678026000218)，说明 IRI 在 VR 干预研究中是被广泛接受的量表。另有一项使用 360° 视频 VR 影响照护者情绪与行为的研究，采用了包含**共情、观点采择与焦虑**的前测／后测问卷设计 [Harvard Scholar](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/seyam/files/using_360-video_virtual_reality_to_influence_caregiver_emotions_and_behaviors_for_childhood_literacy.pdf)；针对动物的态度测量则有**动物态度量表（AAS, Animal Attitude Scale）**的适配与验证研究 [MinCiencias](https://kujane.minciencias.gov.co/Record/UNAB2_4e5c8cf75b12a2287ec705351b382daa)。这些工具足以支撑一个「三天可行」的轻量验证：**5–10 人前测／后测，测量对特定行为的识别率与对居家环境资源的改善意愿。**

**但必须诚实地标出空白。** PLOS ONE 那项研究给出的是**识别能力**的测量（把行为信号判为疼痛的可能性评分），而不是**体验后的行为改变**；iStrayPaws 给出的是**共情**的提升，而不是**问题解决**的提升。截至本次检索，**我没有找到任何一项研究测量过「让饲主以宠物的感官／视角观察自己的家环境」对后续环境改善行为的影响**。这意味着项目的核心价值假设是**推断性的**，而不是已被证实的。

因此三天内最稳妥的验证目标不是「证明饲主更爱宠物」，而是一个**可证伪的窄命题**，例如：「看完该体验后，受试者对 N 个居家环境资源缺口的识别率，从前测的 X% 提升到后测的 Y%」。这一命题的好处是：它直接复用 PLOS ONE 已经验证过的「教育干预能提升行为解读能力」这一前提，测量方法成熟，样本量要求低，而且**失败时的信息量最大**——如果连识别率都不提升，那么整个「以视角换理解」的假设就该被重新审视。

**跨子问题关联**：本子问题的薄弱直接削弱了子问题 1 中「需求真实」到「该产品能解决」之间的跳跃；我把这一点保留在「不确定性与缺口」中，并据此把关，不建议在立项陈述中把「提升理解」说成已验证的效果。

---

### 子问题 6：风险与差异点

**结论：本项目最大的风险不是技术，而是「用了最贵的媒介去讲一件本来只需要图片就能讲清的事」。**

把前述证据汇总，风险按其真实杀伤力排序：

**风险一（最高）：机制—成本错配。** 宠主的付费行为发生在极低成本产品上（两人团队、音频素材部分自采的猫语 App 一度登顶付费榜 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)），而 VR 内容制作需要 360 相机、室内低角度拍摄、性能调优与头显分发，成本高出几个数量级，触达面却小得多（WebXR 在 iOS 不支持 [caniuse](https://caniuse.com/webxr)）。**如果三天后交付的是一个必须戴头显才能体验的 demo，它在立项评审中的说服力可能低于一个能扫码即看的网页。**

**风险二：机制已被占位而团队无差异化叙事。** iStrayPaws 已在 VRST 2024 发表 [ACM](https://dl.acm.org/doi/10.1145/3641825.3687729)。团队若以「首创宠物视角 VR」为话术会被直接推翻；必须转向「家养宠物／居家环境／理解而非同情」这一区间。

**风险三：拟人化学术质疑。** 「代入宠物视角」在动物行为学中是有争议的表述 [Anthropomorphism Revisited](https://comparative-cognition-and-behavior-reviews.org/wp/wp-content/uploads/2013/10/vol_2_commentary_timberlake.pdf)。规避方式是只宣称可核查的感官与资源事实。

**风险四：眩晕与性能。** 90 fps／20–30 ms 是硬门槛，72 fps 即可诱发不适 [LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps)。

**风险五（被团队自己忽略了，但从表格看很明显）：内容制作而非开发才是真正的瓶颈。** 团队打分矩阵里候选 A 在「三天能否完成」上得 2/2/3，是三个候选里唯一被自评拖后腿的维度（B 为 5/5/5）[见立项文档转录](team2_proposal_transcript.md)。这个自评是准确的，但团队仍选了 A，理由偏向「新颖／有代入感」而非可行性。

**差异点（三条，按可辩护程度排序）：**
1. **从「换机位」升级到「换感知系统」。** 竞品 Enabot 已做到贴地视角并证明其内容受欢迎（用户称「老鼠视角」）[人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)，但没人把二色视觉、200° 视野、58 Hz–75 kHz 听阈、`人眼阈值 6 倍`的暗视觉这些**可核查的物种差异**做成体验。这是 Hard-to-copy 的部分，因为它要求动物感官学知识。
2. **站在专业方认可的那一侧。** 猫语翻译类产品被专业行为咨询师批评为不可靠甚至可能有害 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)，而专业方推荐的路径是「声音与肢体动作结合」的观察——视觉／情境化理解是主场。
3. **依附权威框架做可核查的价值。** 用 AAFP/ISFM「五大支柱」与关键资源清单作为内容骨架 [EurekAlert](https://www.eurekalert.org/news-releases/511468) [JFMS/PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10812122/)，使产品从「你感觉猫更舒服了吗」变成「你家缺哪几项资源」。

---

## 对比 Comparison

### 表 1：技术路线对比（三天交付视角）

| 路线 | 需要头显 | 触达面 | 三天可行性 | 主要坑 | 来源 |
|---|:---:|---|---|---|---|
| WebXR + three.js（真 VR） | ✅ 是 | ❌ 极小（iOS Safari 全版本不支持） | 🔴 低 | iOS 无支持；90 fps 性能门槛；设备分发 | [caniuse](https://caniuse.com/webxr)、[LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps) |
| Unity / Unreal 原生 | ✅ 是 | ❌ 极小 | 🔴 极低 | 三天内开发＋打包＋分发不现实 | — |
| 预渲染 360° 视频／图片（浏览器） | ❌ 否 | 🟢 大（扫码即看） | 🟡 中 | 内容拍摄是瓶颈（低角度、弱光、宠物不配合）；沉浸感下降 | [cloudimage-360-video](https://scaleflex.github.io/cloudimage-360-video/)、[Insta360 对比](https://www.trustedreviews.com/versus/insta360-x5-vs-x4) |
| 伪 3D 视差／图像滤镜生成器 | ❌ 否 | 🟢 最大 | 🟢 高 | 沉浸感最弱；但「猫眼中的你家」叙事完整 | — |

### 表 2：竞品与空位

| 玩家 | 类型 | 做什么 | 独立评价 / 局限 | 来源 |
|---|---|---|---|---|
| iStrayPaws（东南大学） | 学术 VR 系统 | 第一人称流浪动物视角，视听＋动觉 | 同行评议验证共情显著提升；对象为流浪动物，非家养宠物 | [ACM VRST 2024](https://dl.acm.org/doi/10.1145/3641825.3687729) |
| 「猫咪语言」及同类猫语 App | 手机 App | 人猫语言双向翻译，订阅 12–68 元/月 | 一度登顶 iOS 付费榜（两人团队）；专家指标准化翻译不可靠、易危险误判 | [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00) |
| MeowTalk（喵语） | 手机 App | 用兽医科研标注数据训练 AI 模型识别猫叫 | 同上，属同一被质疑品类 | [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00) |
| Enabot 陪伴机器人 | 硬件＋App | 全屋移动、语音通话、贴地视角拍摄 | 全球用户破 100 万、160 余国；「老鼠视角」内容受欢迎；**只是机位低，非感官模拟** | [人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html) |
| 寵爾頓 智能舱 | 硬件 | 新风、温控、喂养、监控、互动一体，2000 余元 | 解决异味痛点；与「理解宠物」无关 | [人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html) |
| GoPro Fetch 犬用胸背带 | 硬件配件 | 把运动相机固定在犬背上 | 第一视角拍摄方案；无感官转换、无理解层 | [GoPro](https://gopro.com/es/pe/shop/mounts-accessories/fetch-dog-harness/ADOGM-001.html) |
| 室内宠物摄像头品类 | 硬件 | 远程看护、双向语音 | 品类拥挤、增长约 8.5% CAGR（Tier 3-4 口径） | [格隆汇](https://dxpress.gelonghui.com/p/3266208) |

**对表 1 的解读。** 这张表真正的信息不在任何单格里，而在「需要头显」这一列的分布上：四条路线里有两条要求头显，而这两条的触达面都是「极小」，原因却不是用户不愿意买头显，而是**浏览器层面直接把 iPhone 用户挡在门外**（Safari on iOS 全版本不支持 WebXR）。这一点值得反复强调，因为团队在立项文档里把「VR」写成了产品定义的一部分，等于在尚未评估分发路径的情况下先锁定了最难的那条路。反过来看，下方两条「不需要头显」的路线并非妥协产物——预渲染 360° 与伪 3D 生成器都能保留「以猫的身体尺度重新看家」这个核心叙事，只是把「沉浸」从技术指标降级为程度问题。考虑到宠主主力是 90 后（42.7%）与 00 后（26.3%），扫码即看与分享传播的价值，很可能高于头显带来的那一点临场感。此外，360° 内容路线的真实瓶颈被普遍低估：Insta360 X5 这样的消费级设备在硬件上完全够用（8K/30fps、双 1/1.28 英寸传感器、弱光提升）[Trusted Reviews](https://www.trustedreviews.com/versus/insta360-x5-vs-x4)，但在室内弱光下、以离地 20 厘米的高度、追拍一只不配合的猫，是**独立于开发工作的内容生产难题**，而三天里开发和拍摄会争抢同一批人力。

**对表 2 的解读。** 这张表最值得注意的模式是：**现有玩家几乎全部在做「宠物侧」——摄像头看宠物、穿戴设备测宠物、智能舱养宠物、翻译器解读宠物叫声。** 唯一一个做「饲主侧体验」的 iStrayPaws 是学术项目，且对象是流浪动物；唯一一个已经商业化的「非人类视角」是 Enabot 的贴地机位，但它把视角当成内容素材（「老鼠视角」用于短视频传播），而不是理解工具。**「饲主侧 + 家养宠物 + 自家居家环境 + 感官转换」这四个条件的交集是空的**，而这正是本项目的定位空间。另一个模式同样重要：最热的那条产品线（猫语翻译）之所以热，是因为它把「理解宠物」压缩成了一个**输入输出明确、几乎零成本、可订阅**的动作；本项目若想与之竞争注意力，必须同样提供一个「一眼就懂」的动作，而不是一段需要解释才能理解的沉浸体验——这也再次指向了子问题 4 中「可扫码即看」的路线。

**两张表的交叉含义。** 表 1 说「别把头显当唯一机制」，表 2 说「空位在饲主侧的感官转换」。两者合起来给出的最优解，是一个**不需要头显、以物种感官差异为核心内容、依附五大支柱框架、并把视角作为可视化工具而非情绪渲染**的产品。这个形态恰好也是三天内最可能做成的形态——这是本报告最重要的一个收敛结论。

---

## 矛盾与分歧 Contradictions & Debates

**1. 饲主的自我认知 vs 实测能力。** 宠主普遍相信猫狗「听得懂」「能交流」：英国媒体报道的调查称「近半数宠主确信自己的猫狗理解自己」[Daily Post](https://www.dailypost.co.uk/news/uk-world-news/pet-owners-cat-dog-tendendo-30271862)、「数百万宠主确信自己的猫狗能回话」[Mirror](https://www.mirror.co.uk/lifestyle/pet-owners-cats-and-dogs-34010799)（**注：均为小报转述的宠主调查，未标明样本量与委托方，属 Tier 3，仅作态度侧参考**）；但 PLOS ONE 2026 的对照研究显示，养犬者在**细微信号**识别上并不优于从未养过狗的人 [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)。
**证据权重**：PLOS ONE 是同行评议的对照研究（n=647），权重高于媒体调查。
**结论**：两者并不矛盾，而是揭示了痛点的结构——**不是能力缺失，而是能力错觉**。这一点直接影响立项话术：不应假设用户会主动承认自己「读不懂」，产品需要让差异被看见，而不是被告知。

**2. 猫语翻译 App 厂商宣称 vs 行为专家判断。** 厂商侧：MeowTalk 称其模型基于兽医科研标注数据训练，部分 App 标榜「帮助主人更好地了解猫咪的需求」（尽管角落里标着「仅供娱乐」）；专家侧：孙文认为标准化翻译片面，且**把紧张焦虑的发声误译为平常含义可能导致危险误判**，人语转猫语还可能诱发猫的应激与攻击 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。
**证据权重**：厂商的模型训练说法无法独立验证；专家的判断有十年、3000 余例临床行为矫正经验支撑，且记者实测出现「粮碗是满的却翻译成『我饿了』」的翻车案例。
**结论**：**专家侧证据明显更强。** 值得注意的是，记者实测中「召唤功能几乎每次都能吸引家猫注意」是有效的——这说明**单向的、基于真实录音的刺激**有效，而**双向的语义翻译**不可靠。这个区分对本项目极其有用：如果要碰声音，只能碰「真实录音的单向刺激」，绝不要碰「语义翻译」。

**3. 猫的锥细胞数量：3 种还是 2 种？** 兽医继续教育论文明确写「猫有 3 个锥细胞种群」[VetScienceWeek](http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf)，而主流动物视觉文献通常把猫列为二色视觉（dichromat，蓝＋绿）物种。
**证据权重**：两者都是 Tier 2 级别，且我未能获取该论文引用的原始光学研究。
**结论**：**未解决。** 我选择在报告中只使用更保守的表述（猫的色觉显著不同于人类三色视觉），而不声称猫的锥细胞具体数量。**这条分歧恰好印证了一个方法论要求：凡涉及具体感官数值，产品文案都应回到原始研究核对，而不是相信二手科普。**

**4. 猫的听觉上限：58 Hz–75 kHz 还是 45 Hz–64 kHz？** 2023 年综述的听阈表给出猫 58 Hz–75 kHz，引自 Heffner 与 Heffner 的研究 [Laboratory Animal Research](https://link.springer.com/article/10.1186/s42826-023-00182-3/tables/2)；而该领域被广泛引用的常见数值是 45 Hz–64 kHz。
**证据权重**：综述表格是有引用来源的二手汇总，其引用的原始论文我未能获取全文。
**结论**：**未解决**，差异可能源自测量条件（声压级、判定标准）或转述误差。**实践建议：产品中若展示听觉对比，应使用「犬猫可听频率远高于人类」这一稳健结论，避免把有争议的具体上限当作事实展示。**

**5. VR 眩晕阈值：不同来源口径不一。** 工程实践总结给出「运动到光子延迟 20–30 ms、90 fps 为基线、72 fps 即可诱发不适」[LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps)；而我下载的一篇 2025–2026 年沉浸式视觉质量系统综述则报告，体三维社交 XR 的端到端延迟「超过 900 ms 才显著降低临场感」[Virtual Reality 期刊](https://link-hkg.springer.com/content/pdf/10.1007/s10055-026-01433-z_reference.pdf)。
**证据权重**：两者测量对象不同——前者是本地头显渲染延迟，后者是网络传输的社交 XR 延迟。
**结论**：**不是真矛盾。** 但存在一个对本项目重要的**证据缺口**：我没有找到直接研究「低视角／动物第一视角是否更易诱发眩晕」的文献。这是一个真实的未知，建议在三天原型中预留一次 5 人试戴的耐受性观察。

---

## 不确定性与缺口 Uncertainties & Gaps

- ⚠️ **中国本土的「饲主读不懂宠物」量化数据缺失。** 现有最强证据来自荷兰（PLOS ONE 2026）与英国（PDSA PAW 2024）。跨文化、跨品种效度未经检验，不能直接外推为中国市场的痛点比例。
- ⚠️ **「理解宠物」类消费的付费意愿数据只有间接证据。** 结论建立在猫语 App 登顶 iOS 付费榜的媒体报道上 [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)，而非付费意愿调研。且该产品的成本结构与 VR 内容不可比。
- ⚠️ **核心因果链未被任何研究验证。** 「以宠物视角观察自家环境 → 饲主理解与行为改善」这条链路，未找到直接研究。现有证据只能覆盖前半段（教育干预能提升行为解读）与旁证（第一人称动物 VR 能提升共情）。
- ✅ **【第 2 轮已补齐】PDSA PAW 2024 的具体数值已获取**（58% 独居／42% 多猫、55% vs 48% vs 67%、95% 自认了解环境、约 180 万只猫）。原缺口系因网页版数值仅以信息图呈现，第 2 轮改为下载报告 PDF 并本地提取文本后解决 [PDSA PAW 2024 PDF](https://www.pdsa.org.uk/media/14944/pdsa_paw-report-2024.pdf)。
- ⚠️ **2025–2026 年「非人类具身 VR」研究集群只核实到题录层面，未读全文。** 《Having Dog Ears "for Real"》《Seeing with a Bird's Perception》《Investigating How to Control Virtual Spiders…》等作品的**标题、年份、发表venue** 来自 Semantic Scholar 引文图谱（结构化元数据，可信），但其**具体实验设计、样本量与结论我未获取全文**，因此报告中只用于「赛道正在被填充」这一存在性判断，未引用其任何具体发现。arXiv 查询本次遭遇 HTTP 429，ACM 全文仍被拦截。
- ⚠️ **iStrayPaws 全文始终未获取**（ACM 全文页与 PDF 均被 Cloudflare 403 拦截，第 2 轮尝试的第三方阅读代理亦失败）。因此其**样本量、效应量、实验设计细节仍属未知**；本报告的结论建立在 Semantic Scholar 返回的官方摘要之上，辅以一篇独立系统综述对其方法的描述 [Empathic Computing 综述](https://oss.sciexplor.com/manuscript/329/publish/EC-202501.pdf)。
- ⚠️ **猫的听觉上限与锥细胞数量存在来源冲突**（见「矛盾与分歧」第 3、4 条），未解决。
- ⚠️ **狗的嗅觉数值只有 Tier 3 来源，且文献口径分歧大。** 第 2 轮找到的伊利诺伊大学课程讲义（嗅上皮 18–150 cm² vs 人类 3–4 cm²；受体 >1.5 亿 vs 500 万）**未标注一次文献**，而同类数字在文献中差异很大 [University of Illinois CITL](https://cdn.citl.illinois.edu/courses/ansc207/week2/special_senses/web_data/file10.htm)。原计划的 Tier 1–2 路线全部失败：Frontiers 犬嗅觉综述页面为 JS 渲染无法本地提取，PMC 直连遭遇 SSL 异常与 reCAPTCHA，core.ac.uk 的 PDF 返回 403。**因此报告只使用了量级性的方向结论，未采信任何具体数值。**
- ⚠️ **多个市场规模数据来自付费墙后的商业报告**（宠物可穿戴、室内宠物摄像头、宠物科技市场），本次仅能确认报告存在与中文二手转述的口径（如约 8.5% CAGR），属 Tier 3-4，未独立验证。
- ⚠️ **iStrayPaws 全文未获取。** ACM 全文页被 Cloudflare 拦截（HTTP 403），本次结论全部基于 Semantic Scholar 返回的官方摘要（已逐字核对），未获取其具体实验设计、样本量与效应量。
- ⚠️ **PDSA、AAFP 等机构数据以英文/英国语境为主**，中国宠物行为学（如本土猫品种、居住密度、高层住宅环境）的差异未被覆盖。
- ⚠️ **【检索过程限制】** 本次计划的三个并行检索子代理全部因 API 并发上限（HTTP 429）失败且未产出笔记。**第 2 轮改为串行自查并补回了三个缺口（PAW 2024 数值、五大支柱完整引文、2025–2026 研究集群），置信度由 74% 上调至 80%；但实际检索量仍低于 exhaustive 档位上限（20 次检索／30 来源），且「效果验证」子问题仅 58%，因此仍未达 exhaustive 的 95% 门槛。**

---

## 建议 Recommendations

### 主要建议 Primary Recommendation

**保留「视角转换」作为核心创意，但把「VR」从产品定义降级为候选机制之一，并把三天交付形态定为「不需要头显、扫码即看」的网页体验。**

理由有三条，且都有证据支撑。**第一，需求侧的痛点结构适合「视觉化理解」而不是「声音翻译」**——PLOS ONE 2026 证明饲主的短板是细微信号识别（经验缺口），而专业行为咨询师推荐的正是「声音与肢体结合」的观察路径，恰好是视觉的主场；而最热的声音翻译路线已被专业方指出可能造成危险误判 [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512) [新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。**第二，头显路线在三天内与受众覆盖上双重不利**——WebXR 在 iOS Safari 全版本不受支持，而宠主主力是手机端的 90 后与 00 后；90 fps／20–30 ms 的性能门槛对一个新团队是硬风险 [caniuse](https://caniuse.com/webxr) [LavaPi](https://www.lavapi.com/blog/vr-performance-budgets-90fps) [央视网](https://business.cctv.com/2026/01/05/ARTIdmv2AWmVeRVodaZYLOvQ260105.shtml)。**第三，差异化空位在「感官转换」而不在「沉浸感」**——Enabot 已证明「非人类视角内容」有传播力（「老鼠视角」），但没人把二色视觉、200° 视野、58 Hz–75 kHz 听阈、暗视觉 6 倍阈值这些可核查的物种差异做成体验 [人民网](http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html)。

**具体落地建议（三天）：**
1. **把内容骨架锚定在 AAFP/ISFM「五大支柱」与关键资源清单上**（安全的地方、多个且分离的关键资源、玩耍与捕猎机会、可预测的人猫互动、尊重嗅觉的环境）[EurekAlert](https://www.eurekalert.org/news-releases/511468)，让产品输出从「情绪描述」变成「你家缺哪几项资源」——这是可核查、可验证、且专业方认可的价值。
2. **选一个最强、最反直觉的演示点做主视觉**：推荐「同一客厅在猫的视野与身体尺度下是什么样」，并叠加**闪烁融合频率差异**（人眼约 60 Hz vs 宠物 70–80 Hz，即人看着不闪的灯宠物看着在闪）[VetScienceWeek](http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf)。这一点反直觉、可视觉化、且证据来自兽医继续教育材料。
3. **验证目标写成窄命题**，例如「看后对 N 项居家资源缺口的识别率从前测 X% 提升到后测 Y%」，采用 5–10 人前后测，量表可参考 IRI 与动物态度量表 AAS 的既有用法 [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2949678026000218) [Harvard Scholar](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/seyam/files/using_360-video_virtual_reality_to_influence_caregiver_emotions_and_behaviors_for_childhood_literacy.pdf)。**不要**把验证目标写成「提升饲主对宠物的爱」——那不可证伪。
4. **措辞纪律（针对拟人化风险）**：只说「我们可视化猫的视野／听阈／身体尺度」（可证伪），不说「我们知道猫此刻在想什么」（不可证伪），并在答辩材料中主动引用「批判性拟人化」这一学术概念，把质疑转成专业性展示 [Anthropomorphism Revisited](https://comparative-cognition-and-behavior-reviews.org/wp/wp-content/uploads/2013/10/vol_2_commentary_timberlake.pdf)。
5. **在 60 秒陈述中主动承认先行工作与正在收窄的窗口**：明确说明 iStrayPaws（VRST 2024）已证明第一人称动物 VR 能显著提升共情，且 2025–2026 年已出现一批非人类具身 VR 作品（狗耳朵触觉具身、鸟的感知可穿戴、蜘蛛具身），本项目差异在「家养宠物／饲主自家环境／理解而非同情」[ACM](https://dl.acm.org/doi/10.1145/3641825.3687729) [引文图谱](https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3641825.3687729/citations)。主动承认比被质疑后承认更有说服力，而且「我们知道自己站在谁的肩膀上、也知道窗口在关」本身就是一种专业信号。

### 备选方案 Alternative

**如果团队坚持「必须有 VR 头显」**（例如课程评分明确要求沉浸式技术、或已能稳定借到头显），那么建议：**保留头显体验为「展台版」，同时并行做一条手机端降级路径**，并把三天范围的「必须完成」锁定在「手机端可看」上，头显版作为加分项而非交付底线。触发这个选择的条件是：**现场能拿到头显的真机，且团队中有人此前做过 WebXR 或 Unity**。两个条件缺一，主建议仍然成立。此外，若课程评分更看重技术复杂度而非用户价值，那么应当把这一点明确写进立项陈述——那是评分口径问题，不是产品问题。

### 不建议 Not Recommended

1. **不要加「翻译宠物在说什么」的功能。** 该路线已被专业行为咨询师公开判定为不可靠且可能危险（把焦虑发声误译为平常含义、合成声可能引发应激与攻击）[新闻晨报](https://news.qq.com/rain/a/20260309A07U8S00)。加入这个功能会把项目直接推到专业质疑的火力下，且技术上依赖一个团队三天内无法验证的语义模型。
2. **不要把「VR」当作唯一机制锁死。** 依据是 WebXR 在 iOS Safari 全版本不受支持这一硬事实 [caniuse](https://caniuse.com/webxr)；锁定头显等于锁定最小受众。
3. **不要承诺「让饲主完全读懂宠物」。** PLOS ONE 的研究恰恰说明这类能力是**经验依赖**的、且细微信号识别极难 [PLOS ONE](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512)。承诺过大既不可验证，也正好落入拟人化的批评范围。
4. **不要在未做小样本试戴的情况下把「低视角第一人称」当作无风险设计。** 我未找到任何研究直接检验「动物第一视角是否更易诱发眩晕」，这是一个真实的未知（见「矛盾与分歧」第 5 条）。

---

## 方法 Methodology

- **Depth**：exhaustive（目标档位）。**实际执行量仍低于档位上限**：计划 20 次检索／30 来源，实际完成约 16 次批量检索（含 50 条以上查询）／35 个来源，其中 19 次 `web_fetch` 尝试（11 次取得有效全文）、6 个 PDF 下载后本地提取文本、若干页面经本地下载＋正则抽取以避免摘要失真、1 次 Semantic Scholar 引文图谱查询。**分两轮完成：第 1 轮产出报告初版（置信度 74%），第 2 轮针对三个可修缺口补漏、并对最关键的技术事实做独立交叉验证后将置信度上调至 80%。**
- **最终置信度**：**80%**（低于 exhaustive 的 95% 门槛，原因见下）。分项：需求真实性 85%（Tier 1 PLOS ONE + Tier 2 PAW 全国代表性调查，两条独立证据路径结论一致）／科学依据 82%（Tier 1 指南与综述为主）／竞品与差异化 84%（引文图谱补入 2025–2026 研究集群）／三天可行性 78%／风险与差异点 72%／**效果验证 58%（最低）**。
- **子问题**：定义 6 个；完整回答 4 个（需求真实性、科学依据、竞品与差异化、三天可行性），部分回答 2 个（效果验证 58%、风险与差异点 72%）。
- **多跳检索链**：① 行业报告（央视网/白皮书）→ 消费结构与人群年龄 → 分发渠道含义（手机端优先）；② 需求痛点 → PLOS ONE 原始论文 → 其引用的教育干预证据 → 反推「经验可被人工制造」的立项逻辑；③ VR 机制 → iStrayPaws（VRST 2024）→ 其自述的未覆盖区间（农场动物/野生动物）→ 本项目的差异化区间；④ 猫语 App 热潮（媒体报道）→ 猫行为咨询师批评 → 反推「视觉/情境」路线更稳；⑤ 技术选型 → caniuse WebXR 兼容性表 → iOS 不支持 → 倒逼降级路线；⑥ 宠物视角商业先例 → Enabot「老鼠视角」→ 区分「换机位」与「换感知系统」；⑦ **【第 2 轮新增】iStrayPaws → Semantic Scholar 引文图谱 → 发现 2025–2026 非人类具身 VR 研究集群（狗耳朵触觉具身、鸟的感知可穿戴、蜘蛛具身等）→ 把差异化论证从「邻域空旷」修正为「邻域正在被快速填充」**；⑧ **【第 2 轮新增】PDSA 网页版数值缺失（信息图）→ 直接下载 PAW 2024 报告 PDF → 本地提取文本 → 获得 95% 自认了解 vs 42% 多猫家庭 的对照数字**。
- **来源分级**：Tier 1 = 同行评议论文／官方指南／官方报告（PLOS ONE 2026、JFMS/AAFP 指南、Laboratory Animal Research 综述、ACM VRST 2024、央视网转述的派读白皮书、caniuse、GoPro 官方页）；Tier 2 = 可靠媒体／专业机构／行业媒体（人民网/人民日报海外版、新闻晨报、EurekAlert 新闻稿、VetScienceWeek、PDSA、Trusted Reviews、LavaPi、Semantic Scholar API）；Tier 3-4 = 二手转述与商业报告摘要（格隆汇、市场研究报告索引、评论文章）。
- **关键挑战**：
  1. **三个并行检索子代理全部因 API 并发上限（HTTP 429）失败**，未产出任何笔记，导致实际检索量低于 exhaustive 档位，并直接造成「效果验证」等子问题的证据薄弱。**第 2 轮改为串行自查并补回三个缺口，但该失败仍是本报告未达 95% 置信度的首要原因。**
  2. **两篇最关键的原始文献无法获取全文**：iStrayPaws 的 ACM 全文页被 Cloudflare 拦截（403），第 2 轮尝试的第三方阅读代理亦失败，只能使用 Semantic Scholar 返回的官方摘要；AAFP/ISFM 2013 环境需求指南的 PDF 获取同样被 403 拦截，五大支柱的正式表述改用 EurekAlert 官方新闻稿，**但第 2 轮从 PAW 2024 报告的参考文献中取得了该指南的完整引文**（Ellis SL, Rodan I, Carney HC, Heath S, Rochlitz I, Shearburn LD, … Westropp JL. AAFP and ISFM feline environmental needs guidelines. *J Feline Med Surg* 2013;15(3):219–230）。
  3. **原始文档为图片型 PDF（无文字层）**，通过逐页图像读取转录，手写内容存在辨识误差，已单独产出转录文件供核对。
  4. **多个市场数据位于付费墙后**（宠物可穿戴、室内宠物摄像头、宠物科技市场），无法独立验证。
  5. **PMC 直连受限**：第 2 轮尝试用脚本下载 PMC 页面时遭遇 SSL 异常与 reCAPTCHA，狗的嗅觉量化数值最终仍未取得（详见「不确定性与缺口」）。
- **可复现性材料**：本地已存 `research_notes/`（需求线笔记、原始 PDF 与提取文本、下载页面快照）与 `team2_proposal_transcript.md`（立项文档逐页转录）。

---

## 来源 Sources

| # | 标题 | URL | 日期 | 可信度 |
|---|---|---|---|---|
| 1 | The abilities in dog pain sign recognition…（PLOS ONE, Gardeweg et al., Utrecht University, n=647） | https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0344512 | 2026-04-01 | ⭐ Tier 1 |
| 2 | 《2026 年中国宠物行业白皮书（消费报告）》要点（央视网转载，派读宠物出品） | https://business.cctv.com/2026/01/05/ARTIdmv2AWmVeRVodaZYLOvQ260105.shtml | 2026-01-05 | ⭐ Tier 1 |
| 3 | 2021 AAFP Feline Senior Care Guidelines（JFMS 23(7):613–638，含五大支柱与居家资源清单） | https://pmc.ncbi.nlm.nih.gov/articles/PMC10812122/ | 2021-06-25 | ⭐ Tier 1 |
| 4 | Hearing range table（Sheep as a large animal model for hearing research, Lab Anim Res） | https://link.springer.com/article/10.1186/s42826-023-00182-3/tables/2 | 2023 | ⭐ Tier 1 |
| 5 | iStrayPaws: Immersing in a Stray Animal's World through First-Person VR（ACM VRST 2024，摘要经 Semantic Scholar 核实） | https://dl.acm.org/doi/10.1145/3641825.3687729 | 2024 | ⭐ Tier 1 |
| 6 | WebXR Device API 浏览器兼容性表（caniuse） | https://caniuse.com/webxr | 2026-10 查询 | ⭐ Tier 1 |
| 7 | Fetch: 犬用胸背带（GoPro 官方产品页） | https://gopro.com/es/pe/shop/mounts-accessories/fetch-dog-harness/ADOGM-001.html | 2026-10 查询 | ⭐ Tier 1 |
| 8 | Feline behavior experts release guidelines…（AAFP/ISFM 环境需求指南五大支柱，EurekAlert 新闻稿） | https://www.eurekalert.org/news-releases/511468 | 2013-06-18 | 🔵 Tier 2 |
| 9 | AI能听懂「喵星人」的心声？「猫语」翻译软件大量出现，专家：单纯依靠声音翻译不准（新闻晨报/腾讯新闻） | https://news.qq.com/rain/a/20260309A07U8S00 | 2026-03-09 | 🔵 Tier 2 |
| 10 | 當萌寵遇上智能科技——寵物智能用品品牌發展觀察（人民網／人民日報海外版） | http://sc.people.com.cn/BIG5/n2/2025/1017/c345167-41382842.html | 2025-10-17 | 🔵 Tier 2 |
| 11 | Do dogs really see in black & white? Facts & myths about animal vision（VetScienceWeek） | http://vetscienceweek.com.au/Microsite/pdf/full-paper_108.pdf | — | 🔵 Tier 2 |
| 12 | The PAW Report 2024（PDSA 动物福利报告，YouGov 全国代表性调查） | https://www.pdsa.org.uk/what-we-do/pdsa-animal-wellbeing-report/paw-report-2024 | 2024 | 🔵 Tier 2 |
| 13 | Performance Budgets for VR: Hitting 90fps or Paying the Sickness Tax（LavaPi） | https://www.lavapi.com/blog/vr-performance-budgets-90fps | 2026-03-22 | 🔵 Tier 2 |
| 14 | Insta360 X5 vs X4: What's new?（Trusted Reviews） | https://www.trustedreviews.com/versus/insta360-x5-vs-x4 | 2025 | 🔵 Tier 2 |
| 15 | Anthropomorphism Revisited（Comparative Cognition & Behavior Reviews，讨论 Burghardt 的 critical anthropomorphism） | https://comparative-cognition-and-behavior-reviews.org/wp/wp-content/uploads/2013/10/vol_2_commentary_timberlake.pdf | 2007 | 🔵 Tier 2 |
| 16 | Semantic Scholar Graph API 元数据（iStrayPaws 官方摘要与作者/会议信息） | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3641825.3687729 | 2026-10-02 查询 | 🔵 Tier 2 |
| 17 | @cloudimage/360-video — Interactive 360° Video Player on Three.js（可复用开源组件） | https://scaleflex.github.io/cloudimage-360-video/ | 2026-10 查询 | 🔵 Tier 2 |
| 18 | Akamai AMP A-Frame 360 播放器配置文档 | http://mdtp-a.akamaihd.net/docs/web/amp-web-aframe/akamai.amp.aframe.AframeConfig.html | 2026-10 查询 | 🔵 Tier 2 |
| 19 | Using 360 video VR to influence caregiver emotions and behaviors（含共情／观点采择前后测问卷设计） | https://scholar.harvard.edu/sites/scholar.harvard.edu/files/seyam/files/using_360-video_virtual_reality_to_influence_caregiver_emotions_and_behaviors_for_childhood_literacy.pdf | — | 🔵 Tier 2 |
| 20 | Effectiveness of a mentalisation-based VR group intervention: RCT（使用 IRI 人际反应指针） | https://www.sciencedirect.com/science/article/pii/S2949678026000218 | 2026 | ⭐ Tier 1 |
| 21 | 2025-2031 年家用室内宠物摄像机增长趋势分析（约 8.5% CAGR，中文二手转述） | https://dxpress.gelonghui.com/p/3266208 | 2025 | 🟡 Tier 3 |
| 22 | Adaptación y validación de la escala de actitud hacia los animales (AAS) | https://kujane.minciencias.gov.co/Record/UNAB2_4e5c8cf75b12a2287ec705351b382daa | — | 🟡 Tier 3 |
| 23 | Global Indoor Pet Camera Market Growth 2026-2032（商业报告索引，付费墙） | https://www.marketresearch.com/LP-Information-Inc-v4134/Global-Indoor-Pet-Camera-Growth-45543594/ | 2026 | 🔴 Tier 4 |
| 24 | A systematic review of visual quality in immersive systems（Virtual Reality 期刊，延迟阈值 900 ms 口径） | https://link-hkg.springer.com/content/pdf/10.1007/s10055-026-01433-z_reference.pdf | 2026 | ⭐ Tier 1 |
| 25 | Nearly half of pet owners say their dog or cat understands them（小报转述的宠主调查，样本与委托方未标明） | https://www.dailypost.co.uk/news/uk-world-news/pet-owners-cat-dog-tendendo-30271862 | — | 🟡 Tier 3 |
| 26 | Millions of pet owners are convinced their cats and dogs can talk back（同上，Tier 3，仅作态度侧参考） | https://www.mirror.co.uk/lifestyle/pet-owners-cats-and-dogs-34010799 | — | 🟡 Tier 3 |
| 27 | PDSA PAW Report 2024 **完整报告 PDF**（第 2 轮新增：数值来源，58%/42%/55%/48%/67%/95%） | https://www.pdsa.org.uk/media/14944/pdsa_paw-report-2024.pdf | 2024 | 🔵 Tier 2 |
| 28 | Ellis SL, Rodan I, Carney HC, Heath S, Rochlitz I, Shearburn LD, … Westropp JL. AAFP and ISFM Feline Environmental Needs Guidelines. *J Feline Med Surg* 2013;15(3):219–230（五大支柱原始文献；引文经 PAW 2024 参考文献表核对） | https://doi.org/10.1177/1098612X13477536 | 2013 | ⭐ Tier 1 |
| 29 | Semantic Scholar 引文图谱查询（iStrayPaws 的施引文献，用于发现 2025–2026 非人类具身 VR 研究集群） | https://api.semanticscholar.org/graph/v1/paper/DOI:10.1145/3641825.3687729/citations | 2026-10-02 查询 | 🔵 Tier 2 |
| 30 | A systematic review of using immersive technologies for empathic computing from 2000–2024（Empathic Computing，开放获取，含跨物种共情与 iStrayPaws 的方法描述） | https://oss.sciexplor.com/manuscript/329/publish/EC-202501.pdf | 2025 | ⭐ Tier 1 |
| 31 | Seeing with a Bird's Perception: Designing a Wearable Experience to Reorient Attention to Everyday Nature（CHI EA 2026；**题录级，未读全文**） | https://doi.org/10.1145/3772363.3798350 | 2026 | ⭐ Tier 1（venue）／未读全文 |
| 32 | Investigating How to Control Virtual Spiders While Embodying Them in Virtual Reality（VRST 2025；**题录级，未读全文**） | https://dl.acm.org/doi/pdf/10.1145/3756884.3765989 | 2025 | ⭐ Tier 1（venue）／未读全文 |
| 33 | MDN Web Docs: WebXR Device API（第 2 轮新增；独立交叉验证「非基线、在部分主流浏览器不可用」） | https://developer.mozilla.org/en-US/docs/Web/API/WebXR_Device_API | 2026-10-02 查询 | ⭐ Tier 1 |
| 34 | University of Illinois CITL, ANSC 207《Special Senses》讲义：The dog's olfaction（嗅上皮与受体数量；**Tier 3 教学材料，无一次文献标注**） | https://cdn.citl.illinois.edu/courses/ansc207/week2/special_senses/web_data/file10.htm | — | 🟡 Tier 3 |
| 35 | Safari 27 Beta Release Notes（Apple 官方；**未提及 WebXR**，但页面可能由脚本渲染，仅作弱旁证） | https://developer.apple.com/documentation/safari-release-notes/safari-27-release-notes | 2026 | ⭐ Tier 1／弱旁证 |

---

*本报告为研究产物，不含实现建议之外的代码或架构决策。三个技术路线的最终选择、三天范围的取舍，由 Team 2 自行决定。*
