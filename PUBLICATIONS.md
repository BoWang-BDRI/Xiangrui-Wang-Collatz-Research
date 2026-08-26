# Publications

This page indexes the archived papers associated with the public Collatz mathematics program led by **Xiangrui Wang** at the **Bipolar-Dynamics Research Institute (BDRI)**.

## 1. Layer I — Local control completeness

### The Minimal Positive Odd Pair {1,3} and Local Control Completeness in the Mixed Odd Maps 3n+1 and 3n+3

- **Author:** Xiangrui Wang
- **Main result:** Wang Minimal Positive Odd-Pair Complete Control Theorem (W-MPOCCT)
- **Status:** PROVED / FROZEN within its stated positive-integer domain
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22096604

## 2. Layer II — Positive four-mode global control completeness

### English paper

**From Local Selector Completeness to Global Control Completeness in the Four-Mode Odd System**

- **Author:** Xiangrui Wang
- **Main result:** Four-Mode Odd-System Global Control Completeness Theorem
- **Status:** PROVED / FROZEN
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22104057

### 中文论文

**《从局部选择完备到全局控制完备：四模式正奇数系统的构造性定理》**

- **作者：** Xiangrui Wang
- **主要结果：** 四模式正奇数系统全局控制完备定理
- **状态：** PROVED / FROZEN
- **Zenodo DOI：** https://doi.org/10.5281/zenodo.22104101

## 3. Layer IV — W-NIGECT / nonzero-integer global exact control

The W-NIGECT theorem is archived in separate English and Chinese records.

### English paper

**Global Exact Controllability of the Nonzero-Integer Microdynamics under Signed Affine Controls and Forced Halving**

- **Author:** Xiangrui Wang
- **Main result:** Wang Nonzero Integer Global Exact Control Theorem (W-NIGECT)
- **Active control domain:** \(\mathbb Z\setminus\{0\}\)
- **Target domain:** all integers \(\mathbb Z\)
- **Status:** PROVED / FROZEN
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22109060

### 中文论文

**《带符号仿射控制与强制二分下非零整数微动力的全局精确可控性》**

- **作者：** Xiangrui Wang
- **主要结果：** 王氏非零整数全局精确控制定理（W-NIGECT）
- **活动控制域：** \(\mathbb Z\setminus\{0\}\)
- **目标域：** 全部整数 \(\mathbb Z\)
- **状态：** PROVED / FROZEN
- **Zenodo DOI：** https://doi.org/10.5281/zenodo.22108987

## Scope boundary

The W-NIGECT paper proves global exact controllability of the controlled nonzero-integer microdynamics. It also proves a separate all-integer exact-targetability corollary from any nonzero source, where \(0\) is a terminal target but not an active control state.

```text
CONTROL_DOMAIN = NONZERO_INTEGERS
TARGET_DOMAIN = ALL_INTEGERS

ZERO = VALID_TERMINAL_TARGET
ZERO = NOT_AN_ACTIVE_CONTROL_STATE
NO_TRANSITION_IS_DEFINED_FROM_ZERO

NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN

GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
```
