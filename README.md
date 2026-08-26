# Xiangrui Wang — Collatz Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Collatz-type discrete dynamics** led by **Xiangrui Wang**, Researcher at the **Bipolar-Dynamics Research Institute (BDRI)**.

**Researcher:** Xiangrui Wang  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research area:** Collatz-type dynamics, arithmetic dynamics, controlled odd maps, signed affine control, dyadic microdynamics  
**Contact:** xljun521521@gmail.com

## Research hierarchy

### Layer I — Fixed multiplier 3: local control completeness

For positive odd integers, define

\[
U_c(n)=\operatorname{oddpart}(3n+c),\qquad c\in\{1,3\}.
\]

The **Wang Minimal Positive Odd-Pair Complete Control Theorem (W-MPOCCT)** is **PROVED / FROZEN**. It establishes local control-option completeness for the complementary selectors \(+1,+3\).

See [the W-MPOCCT overview](docs/theorem-overview.md).

### Layer II — Positive four-mode odd system: global control completeness

Define

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),
\qquad (\mu,c)\in\{1,3\}\times\{1,3\}.
\]

The **Four-Mode Odd-System Global Control Completeness Theorem** is **PROVED / FROZEN**. Its constructive consequences include global reset, arbitrary positive-odd targeting, strong connectivity, universal exact cycle embedding, and escape control.

See [the four-mode theorem overview](docs/four-mode-global-control-theorem.md).

### Layer III — Signed odd control

On nonzero odd states, allow signed affine controls with

\[
\mu\in\{1,3\},\qquad c\in\{-3,-1,1,3\}.
\]

Sign reflection is an exact conjugacy, not time reversal. The positive and negative odd half-axes are connected by the explicit bridges

\[
1\to-2\to-1,
\qquad
-1\to2\to1.
\]

The resulting signed odd control graph is globally strongly connected.

### Layer IV — Nonzero-integer exact micro-control

Expose the integer microdynamics:

- **nonzero odd states:** controlled affine step \(n\mapsto\mu n+c\);
- **nonzero even states:** forced halving \(n\mapsto n/2\).

The **Wang Nonzero Integer Global Exact Control Theorem (W-NIGECT)** is **PROVED / FROZEN**:

\[
\forall X,Y\in\mathbb Z\setminus\{0\},\qquad X\leadsto Y.
\]

The active control domain is \(\mathbb Z\setminus\{0\}\), while the exact target domain is all of \(\mathbb Z\). Zero is a **valid terminal target**, but not an active control state; no transition is defined from zero.

Accordingly, the separate **Wang All-Integer Exact Targetability Corollary** gives

\[
\forall X\in\mathbb Z\setminus\{0\},\ \forall Y\in\mathbb Z,\qquad X\leadsto Y.
\]

See [the W-NIGECT theorem overview](docs/w-nigect-global-exact-control-theorem.md).

### Layer V — Standard Collatz: unique passive route, open universal outcome

The standard accelerated Collatz map fixes

\[
T(n)=\operatorname{oddpart}(3n+1).
\]

Its forward route from each initial state is unique by definition. The universal outcome question

\[
\forall n>0\text{ odd},\ \exists k\ge0:\ T^k(n)=1\ ?
\]

is exactly the classical Collatz conjecture and remains **OPEN**.

## Publications and archived papers

### Layer I

- **The Minimal Positive Odd Pair {1,3} and Local Control Completeness in the Mixed Odd Maps 3n+1 and 3n+3**  
  DOI: https://doi.org/10.5281/zenodo.22096604

### Layer II

- **English:** *From Local Selector Completeness to Global Control Completeness in the Four-Mode Odd System*  
  DOI: https://doi.org/10.5281/zenodo.22104057
- **中文：**《从局部选择完备到全局控制完备：四模式正奇数系统的构造性定理》  
  DOI: https://doi.org/10.5281/zenodo.22104101

### Layer IV — W-NIGECT

- **English:** *Global Exact Controllability of the Nonzero-Integer Microdynamics under Signed Affine Controls and Forced Halving*  
  DOI: https://doi.org/10.5281/zenodo.22109060
- **中文：**《带符号仿射控制与强制二分下非零整数微动力的全局精确可控性》  
  DOI: https://doi.org/10.5281/zenodo.22108987

See the complete [publication index](PUBLICATIONS.md).

## Absolute mathematical guardrails

```text
CONTROL_DOMAIN = NONZERO_INTEGERS
TARGET_DOMAIN = ALL_INTEGERS

ZERO = VALID_TERMINAL_TARGET
ZERO = NOT_AN_ACTIVE_CONTROL_STATE
NO_TRANSITION_IS_DEFINED_FROM_ZERO

NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN

SIGN_MIRROR != TIME_REVERSAL

GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
