# Xiangrui Wang — Collatz Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Collatz-type discrete dynamics** led by **Xiangrui Wang**, Researcher at the **Bipolar-Dynamics Research Institute (BDRI)**.

**Researcher:** Xiangrui Wang  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research area:** Collatz-type dynamics, arithmetic dynamics, controlled odd maps, signed affine control, dyadic base maps, normalization ports, exact inverse dynamics  
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

Sign reflection is an exact conjugacy, not time reversal. The positive and negative odd half-axes are connected by explicit bridges, and the resulting signed odd control graph is globally strongly connected.

### Layer IV — Nonzero-integer exact micro-control

Expose the integer microdynamics:

- **nonzero odd states:** controlled affine step \(n\mapsto\mu n+c\);
- **nonzero even states:** forced halving \(n\mapsto n/2\).

The **Wang Nonzero Integer Global Exact Control Theorem (W-NIGECT)** is **PROVED / FROZEN**:

\[
\forall X,Y\in\mathbb Z\setminus\{0\},\qquad X\leadsto Y.
\]

Zero is a valid terminal target but not an active control state.

See [the W-NIGECT theorem overview](docs/w-nigect-global-exact-control-theorem.md).

### Layer V — Standard accelerated Collatz: dyadic base map, threefold folding, entrance transfer, and project global completeness

The current standard-map program is organized around two exact odd maps:

\[
A(n)=\operatorname{oddpart}(n+1),
\qquad
U(n)=\operatorname{oddpart}(3n+1).
\]

Every positive odd integer has the unique dyadic address

\[
\boxed{n=2^aq-1},\qquad q=A(n)<n,
\]

so the power lifts

\[
P_a(q)=2^aq-1
\]

form a complete dyadic base tree.

The standard accelerated edge grammar is

\[
\boxed{U(p)=q\iff3p+1=2^bq\iff p=\frac{2^bq-1}{3}}.
\]

The \(3N+1\) action on a power column satisfies

\[
\boxed{U(P_a(q))=P_{a-1}(3q)}\qquad(a\ge2),
\]

and the complete deformation block is

\[
\boxed{U^a(P_a(q))=\operatorname{oddpart}(3^aq-1)}.
\]

All direct-to-root odd states are

\[
\boxed{G_m=\frac{4^m-1}{3}},
\]

with

\[
\nu_3(G_m)=\nu_3(m),
\]

yielding the exhaustive **ROOT / LIVE / SOURCE** entrance classification.

The current project proof then combines complete dyadic generation, exact interface grammar, power-depth deformation, finite inverse words, merge-suffix inheritance, and rooted-suffix closure under every power lift to obtain a project-level rooted-suffix totality theorem.

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
PROJECT_PROOF_ARCHIVED_ON_ZENODO = YES
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
```

This repository distinguishes the author's frozen project proof from independent community acceptance.

See [the Layer V structural overview](docs/dyadic-base-map-threefold-folding-global-completeness.md).

## Current continuation — exact finite valuation geometry

The next series is separated from the global-completeness paper. Current finite exact objects include

\[
2^{A_K}n_K=3^Kn_0+C_w,
\]

\[
P_w=2^{A_K}-3^K,
\qquad
H_w(n_0)=C_w-P_wn_0,
\]

with

\[
2^{A_K}(n_K-n_0)=H_w(n_0).
\]

The first paper in this continuation has now been archived on Zenodo:

**Exact Valuation Geometry and Root-Anchored Certificates for the Accelerated Collatz Map I: Affine Height, Dyadic Normalization Ports, and Finite Inverse Words**  
DOI: https://doi.org/10.5281/zenodo.22197750

The active continuation includes partial dyadic tails, root-anchored exact certificates, port-resolved inverse genealogy, MergeDAG organization, and structural translation of finite parity/stopping-window phenomena.

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

### Layer V — Standard accelerated Collatz

- **English:** *Dyadic Base Map, Threefold Folding, Entrance Transfer, and Global Completeness in the Accelerated Collatz Odd System*  
  DOI: https://doi.org/10.5281/zenodo.22182820
- **中文：**《加速考拉兹奇数系统的二幂底图、三倍折叠、入口迁移与全局完备性》  
  DOI: https://doi.org/10.5281/zenodo.22182736

### Layer VI — Exact finite valuation geometry

- **English:** *Exact Valuation Geometry and Root-Anchored Certificates for the Accelerated Collatz Map I: Affine Height, Dyadic Normalization Ports, and Finite Inverse Words*  
  DOI: https://doi.org/10.5281/zenodo.22197750

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

PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
PROJECT_PROOF_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE

THIS_PAPER_GLOBAL_CLAIM = NONE
W-NIGECT != STANDARD_COLLATZ_PROOF
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
