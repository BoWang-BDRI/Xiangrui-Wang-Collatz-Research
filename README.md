# Xiangrui Wang — Collatz Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Collatz-type discrete dynamics** led by **Xiangrui Wang**, Researcher at the **Bipolar-Dynamics Research Institute (BDRI)**.

**Researcher:** Xiangrui Wang  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research area:** Collatz-type dynamics, arithmetic dynamics, controlled odd maps, dyadic normalization  
**Contact:** xljun521521@gmail.com

## Research hierarchy

### Layer I — Fixed multiplier \(3\): local control completeness

For positive odd integers \(\Omega=\mathbb N_{\mathrm{odd}}^{+}\), define

\[
U_c(n)=\operatorname{oddpart}(3n+c),\qquad c\in\{1,3\}.
\]

The **Wang Minimal Positive Odd-Pair Complete Control Theorem (W-MPOCCT)** is **PROVED / FROZEN**. It establishes local control-option completeness for the complementary selectors \(+1,+3\): one shallow gate, one folding gate, both local height signs, and the exact mod-3 odd-image partition.

> In Layer I, “complete” means local control-option completeness only. It does not imply global strong connectivity.

See [the W-MPOCCT overview](docs/theorem-overview.md).

### Layer II — Four-mode system: global control completeness

Define the exact four-mode positive-odd system

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),
\qquad (\mu,c)\in\{1,3\}\times\{1,3\}.
\]

The dyadic exponent is always the exact state-determined valuation \(\nu_2(\mu n+c)\); it is not a free control parameter.

The **Four-Mode Odd-System Global Control Completeness Theorem** is **PROVED / FROZEN** after independent red-team audit. Its constructive core is:

- **Global reset:** repeated \((1,1)\) sends every positive odd state to \(1\).
- **Uniform smaller target source:** every odd target \(N>1\) has a positive odd source \(p<8N/9\) that reaches \(N\) in at most three exact control steps.
- **Global generation:** strong induction gives \(1\leadsto N\) for every positive odd \(N\).
- **Global strong connectivity:** \(x\leadsto1\leadsto y\) for all positive odd \(x,y\).
- **Universal exact cycle embedding:** every positive odd state lies on a finite nontrivial exact controlled cycle.
- **Global escape control:** the \(\mu=3\) shallow branch gives an exact escaping trajectory.

See [the four-mode theorem overview](docs/four-mode-global-control-theorem.md).

### Layer III — Standard Collatz: unique passive route, open universal outcome

The standard accelerated Collatz map is the single fixed mode

\[
T(n)=V_{3,1}(n)=\operatorname{oddpart}(3n+1).
\]

Fixing both control coordinates makes the forward route from each initial state unique. This route uniqueness is **definitional**.

The remaining global question is different:

\[
\forall n\in\Omega,\ \exists k\ge0:\ T^k(n)=1\ ?
\]

This **Universal Passive Outcome Problem** is exactly the classical Collatz conjecture and remains **OPEN**.

## Disposition of earlier conjectures

### RESOLVED IN THE FOUR-MODE SYSTEM

- outward reachability;
- global strong connectivity;
- universal closed-walk embedding;
- universal target simple-cycle embedding;
- the four-mode analogue of global control completeness.

### BYPASSED / NOT REQUIRED for the four-mode global proof

The following remain mathematically open as standalone statements, but are no longer prerequisites for the four-mode theorem:

- PLDT;
- MPD18;
- pure-\(F\) non-descending periodicity;
- pure-\(F\) cycle classification;
- higher \(\nu_3=2\) residue-cylinder closure.

### RETAINED OPEN

- standard fixed-\((3,1)\) Collatz global reset;
- fixed-\(+3\) global reset (Collatz-equivalent);
- the original fixed-multiplier \(\mu=3\), \(+1/+3\) global-control conjecture;
- stronger anchored-simple-cycle questions;
- universal passive outcome \(=1\).

See [research status](RESEARCH_STATUS.md), [open problems](docs/open-problems.md), and [public claims boundary](PUBLIC_CLAIMS_BOUNDARY.md).

## Publications and archived papers

### Layer I companion paper

- **The Minimal Positive Odd Pair {1,3} and Local Control Completeness in the Mixed Odd Maps 3n+1 and 3n+3**  
  DOI: https://doi.org/10.5281/zenodo.22096604

### Layer II four-mode global-control paper

- **English:** *From Local Selector Completeness to Global Control Completeness in the Four-Mode Odd System*  
  DOI: https://doi.org/10.5281/zenodo.22104057
- **中文：**《从局部选择完备到全局控制完备：四模式正奇数系统的构造性定理》  
  DOI: https://doi.org/10.5281/zenodo.22104101

See the complete [publication index](PUBLICATIONS.md).

## Absolute mathematical guardrails

```text
DOMAIN = POSITIVE_INTEGERS_ONLY
ODD_STATE_DOMAIN = N_ODD_POSITIVE
NEGATIVE_RATIONAL_REAL_PADIC_OBJECTS = OUTSIDE_THEOREM_DOMAIN

GLOBAL_COLLATZ = OPEN
FOUR_MODE_GLOBAL_CONTROL != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
DUAL/MIXED_CONTROLLED_CYCLE != STANDARD_COLLATZ_COUNTEREXAMPLE
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
