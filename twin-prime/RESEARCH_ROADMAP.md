# 孪生素数研究路线｜Twin-Prime Research Roadmap

**Researcher:** Xiangrui Wang  
**Current canonical paper:** *Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1*  
**Current version:** v2.0  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22851583  
**Last roadmap consolidation:** 2026-09-20

> 本文件不是重新发明一套证明，而是把 Google Drive 中 2026-09-07 至 2026-09-20 的孪生素数研究记录按数学功能、时间顺序和当前状态压缩成一条可追踪研究路线。历史文件中的旧标签保留其当时语义；若后续研究修正了边界、量词或证明地位，以后续冻结节点和当前 v2.0 结构为准。

---

## 0. 当前总图

当前研究主线已经压缩为：

\[
\boxed{
\text{odd-composite source structure}
\to
\text{mod-6 twin windows}
\to
\text{prime-square activation / frozen prefixes}
\to
L_{TS}
\to
(C0,C1)
}
\]

其中强精确定位算子

\[
L_{TS}(p,q)
\]

与两个核心候选定理绑定：

\[
\boxed{C0:\ L_{TS}(p,q)\ge2},
\qquad
\boxed{C1:\ L_{TS}(p,q)\ge q-p},
\]

定义域均为连续素数 \(5<p<q\)，且

\[
C1\Rightarrow C0.
\]

项目内部已完成底层结构、定位算子、first-owner/overlap/CRT 工具和大量有限红队攻击；当前对外数学边界仍是：**C0/C1 的无限全称解析认证需要独立审核**。有限扫描无反例不能替代该全称证明。

---

# I. 第一阶段：底层乘法排列与占位生成

**时间：2026-09-07 起**  
**核心源文件：**《孪生素数研究｜底层乘法排列与占位生成基线 v0.1》

### 研究转向

研究从“素数密度/概率/筛法”转向保留全部生成来源的底层表示：

1. 自然数位置先存在；
2. 非平凡奇数乘法排列按固定顺序占据后续位置；
3. 被占位置为合数，未被任何合法乘法来源占据的奇数位置为素数；
4. 合数层、多源重合、重复来源不删除；
5. 孪生素数不是独立生成对象，而是同一窗口两格同时保持零占位的结果。

固定轨道逐步写成

\[
G_a(k)=a(a+2k)=a^2+2ak.
\]

这一阶段建立了后续全部工作的底层语义：**source-resolved occupancy**。

### 六空间与四状态

3 的倍数形成边界，内部候选位置为

\[
W_n=(6n-1,6n+1).
\]

窗口只有四个排他状态：

- EE：双空，孪生素数；
- EO / OE：单素数；
- OO：双占。

### 第一批红队修正

100k 独立公式审核发现旧任务规格把普通窗口从 \(m\ge3\) 开始，遗漏 \((5,7)\)。修正为 \(m\ge1\) 后：

- \((5,7)\) 由普通 EE 机制生成；
- \((3,5)\) 是唯一前置特殊对；
- 100000 内主体占位集合与独立奇合数集合完全一致；
- 红队结论：主体 PASS，原任务边界规格 FAIL，边界修正 PASS。

**阶段成果：** 把“素数/孪生素数”转化成可逐点复核的占位状态，而不是统计对象。

---

# II. 第二阶段：全局奇合数占位、平方激活与边界自适应扩展

**时间：2026-09-07—09**  
**核心源文件：**

- 《孪生素数生成完备分析｜孪生素数全覆盖定理｜闭合全覆盖版 v0.5》
- 《孪生素数生成完备分析｜顺序占位与边界自适应扩展｜投稿冻结版 v0.6》
- 《孪生素数｜边界自适应扩展四向等价定理｜v0.1》

### 全局奇合数占位恒等

定义

\[
C=\{a(a+2k):a\ge3\text{ odd},\ k\ge0\}.
\]

得到

\[
n\notin C
\iff
n\text{ 为奇素数}.
\]

### Prime-square activation

定义首次新增集合 \(E_a\)。研究冻结出：

- 奇合数基数层只重复更早来源；
- 新素数 source \(p\) 的首次独立新增从 \(p^2\) 开始；
- 后续 source 只能新增或重合，不能回写已完成旧区。

因此平方边界不是任意截断，而是新的独立 least-prime-factor source 的激活前沿。

### 有限认证与永久冻结

对阶段边界 \(b\)，构造有限认证域 \(D_b\)。核心逻辑：

\[
D_3\subset D_5\subset D_7\subset\cdots,
\qquad
\bigcup_bD_b=\{\text{全部奇数 }\ge3\}.
\]

每个固定位置最终进入某个有限认证截面，之后状态永久冻结。

### 四向等价：首次把“无限输出”与“边界无界”分开

边界四向等价研究明确区分：

- **域的无界覆盖**：每个位置最终都能被认证；
- **输出的无界继续出现**：任意窗口阈值之后仍出现新的 EE。

这一步修正了早期容易混淆的推理：**认证域覆盖全部奇数轴，本身不等于孪生输出无限。**

**阶段成果：** 完成“生成—认证—冻结”的母结构，并把真正的无限性问题隔离为“新 EE 是否持续产生”。

---

# III. 第三阶段：素数驱动递归占位、多轨交集与 3 边界吸收

**时间：2026-09-10**  
**核心源文件：**

- 《孪生素数｜素数驱动递归占位、3边界延长与多轨交集｜上午研究完整冻结 v0.1》
- 《孪生素数｜3边界吸收与孪生窗口出生机制｜Codex审计 v0.4 复核记录》

### Prime-Driven Recursive Occupancy

研究进一步把完整来源拆成：

\[
\text{prime skeleton}
+
\text{power deepening}
+
\text{composite embedding}
+
\text{multi-track intersections}.
\]

位置的 source multiplicity 被压缩成状态变量 \(m(x)\)，其中

\[
m(x)=0\iff x\text{ 为素数},
\]

而 \(m(x)\ge2\) 记录真实多主轨交集。

### 3 边界吸收与 2p/4p 节奏

对所有素数 \(p\ge5\)，轨道 \(G_p\) 在模 6 下是严格三周期。每三次 raw hit 中恰有一次落在 3 边界，被记为 **BOUNDARY_ABSORBED**，而不是内部孪生槽打断。

删除边界 hit 后，内部打断距离固定交替为

\[
2p, 4p.
\]

独立 Codex 复核冻结了：

- mod-6 三周期；
- 边界吸收；
- 2p/4p 内部节奏；
- 轨道表示与窗口同余表示等价；
- active-prime avoidance 与真实 EE 分类一致。

**阶段成果：** 从“有哪些位置被占”推进到“prime source 如何以固定节奏进入窗口并发生交集”。

---

# IV. 第四阶段：E1(B) 固定生成闭合与 FG-EE Continuation

**时间：2026-09-12**  
**核心源文件：**《孪生素数｜E1(B)固定生成闭合定理｜顺序平铺与同步扩展 v0.1》

这一阶段尝试把既有 EXACT 结构组装成终局无限性接口。

已冻结部分：

- pointwise prime/composite classification；
- EE/EO/OE/OO 分类；
- 有限认证；
- completed-prefix freeze；
- 无界定义域扩展。

最终缺口被压缩为 **FG-EE Continuation**：有限阶段完成后，在无界同步扩展中是否持续产生新的 EE 输出。

当时的冻结状态：

- FIXED-GENERATION-E1B-ASSEMBLY = FROZEN
- POINTWISE-CLASSIFICATION = EXACT
- E1B = CLOSED-IF-AND-ONLY-IF-FG-EE-CONTINUATION

这一步没有把“未发现尾部停止”当作证明，而是明确要求：

- 要证明 E1(B)，必须从既有顺序占位/交叉公式无循环推出 FG-EE Continuation；
- 要否定，则必须给出完整尾部反例证书。

**阶段成果：** 把早期“全覆盖”措辞降维成一个明确的 continuation bridge。

---

# V. 第五阶段：5–7 走廊、精确覆盖账本与 Final Bridge

**时间：2026-09-17 前后**  
**核心源文件：**

- TwinPrime_Corridor_v0_2_Exact_Audit_Freeze_2026-09-17
- CODEX_TwinPrime_FinalBridge_Audit_Task_v0_3
- 《孪生素数研究｜5–7走廊与Paired-Wheel｜已冻结EXACT定理基线 v0.1》

### 5–7 走廊

定义

\[
I_m=\{x:5m<x<7m, x\equiv\pm1\pmod6\}.
\]

引入精确账本：

- \(B\)：完整孪生候选槽；
- \(H\)：raw source hits；
- \(F\)：不同被占整数位置；
- \(X=H-F\)：整数级多轨重叠损耗；
- \(Y\)：同一孪生槽双端同时被占造成的槽级冗余；
- \(Z\)：边缘无效占位；
- \(W=X+Y+Z\)：总覆盖损耗；
- \(K\)：被真正杀死的不同完整槽；
- \(T=B-K\)：剩余孪生槽。

得到精确恒等式

\[
\boxed{T=B-H+X+Y+Z=B-H+W}.
\]

### 三个关键硬反例关闭错误路线

走廊审核给出：

- \(m=13\)：\(H=B\) 但 \(T=1\)；
- \(m=23\)：\(F=B\) 但 \(T=2\)；
- \(m=49\)：\(F>B\) 但 \(T=3\)。

因此关闭：

\[
H=B\not\Rightarrow T=0,
\qquad
F=B\not\Rightarrow T=0,
\qquad
F>B\not\Rightarrow T=0.
\]

真正的完全覆盖条件只有

\[
K=B
\iff
T=0.
\]

### Final Bridge

最终桥被压缩为

\[
\boxed{W(m)\ge H(m)-B(m)+1},
\]

等价于

\[
\boxed{T(m)\ge1}.
\]

有限全量扫描到 \(m\le9,999,997\) 共 3,333,332 个合法走廊，没有发现 \(T=0\)，但冻结状态仍是：

- STRUCTURAL-IDENTITIES = PASS
- FINITE-T-ZERO-SEARCH = NO COUNTEREXAMPLE
- INFINITE-TWIN-BRIDGE = OPEN

**阶段成果：** 把“覆盖是否会追上空间”精确化为 raw surplus 与 overlap loss 的整数不等式，而不是密度语言。

---

# VI. 第六阶段：Paired-Wheel、CRT No-Go 与 Prime-Square Forest

**时间：2026-09-17—18**  
**核心源文件：**《孪生素数研究｜5–7走廊与 Paired-Wheel｜已冻结 EXACT 定理基线 v0.1》

### Paired-Wheel

研究把每个 prime source 对窗口编号的两个禁止余数类组合成 paired wheel，并冻结：

- paired forbidden residues；
- 周期 \(Q_q\)；
- survivor 精确计数；
- twin-slot survivor 等价；
- phase-local twin criterion；
- wheel lift recursion；
- 多 prime intersection 的 \(2^t\) 个 CRT residue classes；
- overlap inclusion-exclusion。

### CRT No-Go

研究证明：任意**固定有限** entering-zero / entering-all-CC 模式都可以由 CRT 在无界位置构造。

因此关闭了这种证明路线：

> “某个固定有限局部坏模式不可能发生，所以必然存在孪生”。

CRT No-Go 不处理随尺度增长的全带约束或真正非局部不变量。

### Prime-Square Forest

同一冻结基线进一步形成：

- Candidate-Axis Trichotomy；
- Prime-Square Independent Activation；
- Square-Band Fixed-Source Closure；
- Prime-Square Source Relay；
- Activation-Band Owner Product Theorem；
- Twin Cannot Cross a Prime-Square Boundary。

这一组结果为后续从“5–7 走廊”切换到“连续素数平方 band”提供了结构基础。

**阶段成果：** local corridor 与 wheel 工具继续保留，但主证明对象开始向 prime-square band 迁移。

---

# VII. 第七阶段：强精确定位算子 \(L_{TS}\) 与 C0/C1

**时间：2026-09-19**  
**核心源文件：**

- 《孪生素数生成完备分析｜连续素数平方双孪生候选定理｜完整证明结构体 v1.0》
- TwinPrime_C0_Submission_CN_v1_0.pdf
- TwinPrime_Exact_Source_Localization_Full_Submission_v1_3.pdf

### 从“至少一个走廊 survivor”升级到“prime-square 精确计数”

对连续素数 \(5\le p<q\)，定义完整窗口集合 \(\mathcal W(p,q)\)，并定义 single-window exact indicator \(\Theta(n)\)。

强定位算子：

\[
\boxed{
L_{TS}(p,q)=
\sum_{n\in\mathcal W(p,q)}\Theta(n)
}
\]

被证明精确等于开区间 \((p^2,q^2)\) 中实际孪生素数对数量。

### C0 / C1

v1.0 形成：

\[
C0:\quad L_{TS}(p,q)\ge2,
\]

\[
C1:\quad L_{TS}(p,q)\ge q-p.
\]

两者共享同一连续素数定义域、同一强定位算子和同一反例接口。

### v1.3 的数学增强

v1.3 吸收并强化：

- exact first-owner counting；
- activation-band first-owned product structure；
- endpoint overlap / window overlap 分离；
- exact CRT floor-sum locator；
- \(J_2,D_2\) cyclic survivor thresholds；
- 可复现整数回归包。

但 v1.3 的写作层级把 C0 提升为主 candidate theorem，而把 C1 降成 strengthened conjecture。后续 v2.0 已修复这一架构问题。

**阶段成果：** 主承重对象正式变为“强算子 + 两个核心候选定理”。

---

# VIII. 第八阶段：v2.0 统一架构

**时间：2026-09-20**  
**当前 canonical paper：** v2.0  
**DOI:** https://doi.org/10.5281/zenodo.22851583

v2.0 的核心修复是

\[
\boxed{L_{TS}+C0+C1}
\]

三者恢复为同一核心承重模块。

### 当前 EXACT 结构层

1. 奇合数来源完备；
2. 六空间孪生分类；
3. prime-square activation；
4. completed-prefix invariance；
5. consecutive-prime-square finite source completeness；
6. exact band locator \(L_{TS}\)；
7. first-owner identity；
8. endpoint-to-window overlap accounting；
9. CRT floor-sum locator；
10. cyclic survivor tools。

### 两个核心候选定理

\[
C0:\quad L_{TS}(p,q)\ge2,
\]

\[
C1:\quad L_{TS}(p,q)\ge q-p.
\]

由 first-owner identity

\[
L_{TS}=G-F
\]

得到绑定覆盖形式：

\[
C0\iff F\le G-2,
\]

\[
C1\iff F\le G-(q-p).
\]

### 当前逻辑关系

\[
C1\Rightarrow C0,
\]

而一旦 C0 获得完整解析认证，

\[
C0\Rightarrow\text{infinitely many twin primes}.
\]

---

# IX. 历史路线分类

## A. 当前主线继续使用

- \(G_a=a^2+2ak\) source-resolved occupancy；
- 3 边界 / 5 首个普通内部 source；
- 3–5–7 唯一起始重叠；
- prime-square activation；
- finite certification / frozen prefix；
- multitrack intersection provenance；
- exact \(L_{TS}\)；
- first-owner / overlap correction；
- CRT floor-sum；
- C0 / C1。

## B. 已被吸收到主线的工具支线

- 2p/4p internal blocking rhythm；
- 5–7 corridor ledger \(H,F,X,Y,Z,W,K,T\)；
- Paired-Wheel；
- cyclic \(J_2,D_2\)；
- activation-band owner product theorem。

这些工具仍有解释和审核价值，但不再单独承担最终全局结论。

## C. 已被硬反例关闭的推理

- \(H=B\Rightarrow T=0\)；
- \(F=B\Rightarrow T=0\)；
- \(F>B\Rightarrow T=0\)；
- 固定有限 entering-window UNSAT；
- 把所有 EE 归因于“交集重叠”；
- 把认证域无界直接等同于孪生输出无界。

## D. 历史 OPEN-BRIDGE，现由更强表述替代

- FG-EE Continuation；
- 5–7 走廊 \(W\ge H-B+1\)。

它们在历史上精确隔离了“为什么有限认证仍不自动推出无限输出”的缺口。当前主论文用更强、直接绑定真实 twin count 的 C0/C1 表述替代其最终承重角色。

---

# X. 数值证据路线

项目一直维持同一纪律：

\[
\boxed{\text{FINITE AUDIT}\ne\text{UNIVERSAL PROOF}}
\]

主要历史节点：

- 100k 独立公式/试除双链审核；
- 3 边界与 2p/4p 到 \(10^6/10^7\) 的结构审计；
- 5–7 走廊 3,333,332 个合法输入全量搜索；
- 276–285 位 first-EE 内部验证任务规范；
- v1.0 报告的连续 \(p<5\times10^6\) 与高尺度 exact stress；
- v1.3 随稿可复现的 1,226 个正式 prime-square bands 回归。

不同证据包的“可复现随稿证据”和“源文件报告/内部压力测试”不得混为一个证据等级。

---

# XI. 当前审核接口

当前最短研究路线不是继续扩大无反例扫描，而是审核两个全称 bandwise lower bounds：

\[
\boxed{C0:\ L_{TS}(p,q)\ge2},
\]

\[
\boxed{C1:\ L_{TS}(p,q)\ge q-p}.
\]

硬反例格式：

- C0：存在连续素数 \(5<p<q\) 使 \(L_{TS}(p,q)<2\)；
- C1：存在连续素数 \(5<p<q\) 使 \(L_{TS}(p,q)<q-p\)。

证明缺口与定理反例严格分开：

- invalid inference → PROOF NOT ESTABLISHED；
- exact eligible counterexample → candidate theorem falsified。

---

# XII. 一句话压缩

\[
\boxed{
\text{底层奇合数来源}
\to
\text{六空间双空分类}
\to
\text{平方激活与冻结}
\to
\text{多轨/重合/CRT 精确账本}
\to
\text{连续素数平方强定位 }L_{TS}
\to
\text{C0/C1 核心认证}
}
\]

这条路线保留了早期研究的全部承重来源，同时把已经被反例关闭的局部推理与当前真正需要审核的全称命题分离开来。

---

## Source chronology used for this consolidation

The roadmap was consolidated from the following Google Drive research records (titles only; private Drive links/IDs are intentionally not published here):

1. 《孪生素数研究｜底层乘法排列与占位生成基线 v0.1》
2. 《孪生素数研究｜100k公式独立生成红队审核｜边界冲突与主体PASS v0.1》
3. 《孪生素数生成完备分析｜孪生素数全覆盖定理｜闭合全覆盖版 v0.5》
4. 《孪生素数生成完备分析｜顺序占位与边界自适应扩展｜投稿冻结版 v0.6》
5. 《孪生素数｜边界自适应扩展四向等价定理｜v0.1》
6. 《孪生素数｜素数驱动递归占位、3边界延长与多轨交集｜上午研究完整冻结 v0.1》
7. 《孪生素数｜3边界吸收与孪生窗口出生机制｜Codex审计 v0.4 复核记录》
8. 《孪生素数｜E1(B)固定生成闭合定理｜顺序平铺与同步扩展 v0.1》
9. TwinPrime_Corridor_v0_2_Exact_Audit_Freeze_2026-09-17.md
10. CODEX_TwinPrime_FinalBridge_Audit_Task_v0_3.md
11. 《孪生素数研究｜5–7走廊与Paired-Wheel｜已冻结EXACT定理基线 v0.1》
12. 《孪生素数生成完备分析｜连续素数平方双孪生候选定理｜完整证明结构体 v1.0》
13. TwinPrime_Exact_Source_Localization_Full_Submission_v1_3.pdf
14. 《孪生素数｜强定位算子+C0+C1｜完整版投稿论文 v2.0｜2026-09-20》
