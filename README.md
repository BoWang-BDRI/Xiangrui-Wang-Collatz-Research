# Xiangrui Wang — Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Xiangrui Wang** at the **Bipolar-Dynamics Research Institute (BDRI)**. The research program is organized around two complementary mathematical directions: **Collatz Research (Growth Law)** and **Twin Prime Research (Spatial Law)**.

**Researcher:** Xiangrui Wang  
**Motto:** **以凡人之躯，比肩神明，吾之神力，皆源法则！**  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research themes:** Collatz Research (**Growth Law**); Twin Prime Research (**Spatial Law**)  
**Research areas:** Collatz-type dynamics, arithmetic dynamics, exact integer control, dyadic coordinates, inverse dynamics, multiplicative occupancy, prime-generation structure, twin primes  
**Contact:** xljun521521@gmail.com

---

## Quick navigation

| Research branch | Current record | DOI / files |
|---|---|---|
| **Collatz Research — Growth Law** | *A Complete Analysis of the Collatz Conjecture* project record | [10.5281/zenodo.22246883](https://doi.org/10.5281/zenodo.22246883) |
| **Twin Prime Research — Spatial Law** | *Finite-Boundary Adaptive Shells and Exact Multiplicative Occupancy for Twin-Prime Windows* | [10.5281/zenodo.22888216](https://doi.org/10.5281/zenodo.22888216) · [`twin-prime/`](twin-prime/) · [roadmap](twin-prime/RESEARCH_ROADMAP.md) |
| **Integer Arithmetic Growth Laws — Foundation Framework** | *整数四则运算生长法则* | [10.5281/zenodo.22959590](https://doi.org/10.5281/zenodo.22959590) |
| **RB paper** | RB论文 | [10.5281/zenodo.22953186](https://doi.org/10.5281/zenodo.22953186) |
| **Publication index** | Archived research papers | [`PUBLICATIONS.md`](PUBLICATIONS.md) |

---

# Foundation Framework — Integer Arithmetic Growth Laws

## **整数四则运算生长法则**

- **Author:** Xiangrui Wang
- **Role:** foundational framework paper for the arithmetic-growth research program
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22959590

The framework separates a **reference-kernel state space** from separately specified upper-layer arithmetic growth rules. Its first strict branch uses

\[
A(N)=\operatorname{oddpart}(N+1)
\]

on positive odd integers. The foundation paper freezes the following structural layer:

- unique decomposition
  \[
  N=2^a q-1,\qquad a=\nu_2(N+1),\quad q=A(N)<N;
  \]
- strict descent of the reference kernel and finite reachability of the root \(1\);
- exact one-level inverse fibers;
- canonical finite addresses after removal of the degenerate root self-loop;
- root-entry partition \(R_k=2^k-1\) and coverage domains \(C_k\);
- binary block deletion, exact entry classification, dyadic-window counts, and zero-count depth;
- mutually inverse decomposition / generation algorithms and nonredundant bounded enumeration;
- a general affine interface for legal upper-layer branches such as \((mN+c)/d\), without transferring unproved global dynamical claims.

This paper is treated as the **foundation reference** for subsequent branch papers. Upper-layer convergence, cycle structure, first-hit Gate behavior, and other dynamical conclusions remain branch-specific proof obligations.

---

# I. Collatz Mathematics Research — Growth Law

## Research hierarchy

### Layer I — Fixed multiplier 3: local control completeness

For positive odd integers,

\[
U_c(n)=\operatorname{oddpart}(3n+c),\qquad c\in\{1,3\}.
\]

The **Wang Minimal Positive Odd-Pair Complete Control Theorem (W-MPOCCT)** is **PROVED / FROZEN** within its stated domain.

See [the W-MPOCCT overview](docs/theorem-overview.md).

### Layer II — Positive four-mode odd system

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),
\qquad (\mu,c)\in\{1,3\}\times\{1,3\}.
\]

The **Four-Mode Odd-System Global Control Completeness Theorem** is **PROVED / FROZEN**. Its constructive consequences include global reset, arbitrary positive-odd targeting, strong connectivity, universal exact cycle embedding, and escape control.

See [the four-mode theorem overview](docs/four-mode-global-control-theorem.md).

### Layer III — Signed odd control

On nonzero odd states,

\[
\mu\in\{1,3\},\qquad c\in\{-3,-1,1,3\}.
\]

Sign reflection is an exact conjugacy, not time reversal. The positive and negative odd half-axes are connected by explicit bridges.

### Layer IV — Nonzero-integer exact micro-control

- nonzero odd states: controlled affine step \(n\mapsto\mu n+c\);
- nonzero even states: forced halving \(n\mapsto n/2\).

The **Wang Nonzero Integer Global Exact Control Theorem (W-NIGECT)** is **PROVED / FROZEN**:

\[
\forall X,Y\in\mathbb Z\setminus\{0\},\qquad X\leadsto Y.
\]

Zero is a valid terminal target but not an active control state.

See [the W-NIGECT theorem overview](docs/w-nigect-global-exact-control-theorem.md).

### Layer V — Standard accelerated Collatz

Define

\[
A(n)=\operatorname{oddpart}(n+1),
\qquad
U(n)=\operatorname{oddpart}(3n+1).
\]

Every positive odd integer has the unique dyadic address

\[
\boxed{n=2^aq-1},\qquad q=A(n)<n,
\]

with power lifts

\[
P_a(q)=2^aq-1.
\]

The standard accelerated inverse grammar is

\[
\boxed{U(p)=q\iff3p+1=2^bq\iff p=\frac{2^bq-1}{3}}.
\]

The power-column transport is

\[
\boxed{U(P_a(q))=P_{a-1}(3q)}\qquad(a\ge2),
\]

and

\[
\boxed{U^a(P_a(q))=\operatorname{oddpart}(3^aq-1)}.
\]

All direct-to-root odd states are

\[
\boxed{G_m=\frac{4^m-1}{3}},
\]

with

\[
\nu_3(G_m)=\nu_3(m).
\]

The current formulation binds each generated state to its inherited finite standard-\(U\) suffix genealogy. The induction object is therefore a rooted generative object rather than an isolated integer plus an independent residual variable.

**Latest Layer V complete-analysis paper**  
*Dyadic Base Map, Threefold Folding, Rooted Generative Coverage, and Global Normalization in the Accelerated Collatz Odd System (A Complete Analysis of the Collatz Conjecture)*  
DOI: https://doi.org/10.5281/zenodo.22246883

See [the Layer V structural overview](docs/dyadic-base-map-threefold-folding-global-completeness.md).

### Layer VI — Exact finite valuation geometry

The finite exact continuation uses

\[
2^{A_K}n_K=3^Kn_0+C_w,
\]

\[
P_w=2^{A_K}-3^K,
\qquad
H_w(n_0)=C_w-P_wn_0,
\]

and

\[
2^{A_K}(n_K-n_0)=H_w(n_0).
\]

**Exact Valuation Geometry and Root-Anchored Certificates for the Accelerated Collatz Map I: Affine Height, Dyadic Normalization Ports, and Finite Inverse Words**  
DOI: https://doi.org/10.5281/zenodo.22197750

### Collatz status boundary

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
PROJECT_PROOF_ARCHIVED_ON_ZENODO = YES
LATEST_PROJECT_PROOF_DOI = 10.5281/zenodo.22246883
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
PROJECT_PROOF_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE

W-NIGECT != STANDARD_COLLATZ_PROOF
```

---

# II. Twin Prime Research — Spatial Law

## Current paper

### **Finite-Boundary Adaptive Shells and Exact Multiplicative Occupancy for Twin-Prime Windows**

- **Author:** Xiangrui Wang
- **Date:** September 22, 2026
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22888216
- **Research direction:** Twin Prime Research (**Spatial Law**)
- **Research directory:** [`twin-prime/`](twin-prime/)
- **Citation metadata:** [`twin-prime/CITATION.cff`](twin-prime/CITATION.cff)
- **Previous canonical record:** *Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1*, v2.0 — https://doi.org/10.5281/zenodo.22851583

### 1. Continuous admissible shell chain

For every integer \(N\ge2\), define

\[
A_N=3^N,
\qquad
I_N=(A_N,3A_N)=(3^N,3^{N+1}).
\]

The research domain is the continuous chain

\[
I_N\to I_{N+1}\to I_{N+2}\to\cdots .
\]

This shell chain is the spatial backbone of the current twin-prime program.

### 2. Predecessor odd-source projection

The source set contains **all predecessor odd integers**, not only primes:

\[
O_N=\{a:3\le a<A_N,\ a\text{ odd}\}.
\]

A source contributes to the current shell through actual products satisfying

\[
A_N<ab<3A_N,
\qquad b\ge3\text{ odd}.
\]

The union of these products is exactly the set of odd composite positions inside the shell. Prime/composite/twin-prime labels are assigned only after actual landing and deduplication.

### 3. Exact six-window accounting

The complete non-3-divisible windows have total capacity

\[
C_N=3^{N-1}.
\]

Let \(Q_N\) be the number of distinct interrupted windows and \(T_N\) the number of double-free windows. Then

\[
\boxed{T_N=C_N-Q_N=C_N-U_N+D_N},
\]

where \(U_N\) is the number of occupied non-3-divisible endpoints and \(D_N\) is the number of doubly occupied windows.

### 4. Scale-normalized transport and permanent closure

With \(x=a/A_N\), the projection condition becomes

\[
1<xb<3.
\]

The normalized transport rule is independent of the shell scale. Moreover,

\[
a\ge A_N,\quad b\ge3
\quad\Longrightarrow\quad
ab\ge3A_N,
\]

so later sources cannot retroactively fill a completed shell. Each shell therefore freezes permanently after its predecessor projections have been fully processed.

### 5. Current load-bearing theorem

The exact framework reduces the infinitude question along this shell chain to the non-full-coverage condition

\[
\boxed{Q_N<C_N}.
\]

Equivalently, \(T_N\ge1\). If this holds for every admissible shell—or more weakly for infinitely many shells—the permanent double-free windows accumulate across pairwise disjoint shells.

The shell construction, projection completeness, exact accounting, and no-retroactive-fill property are separated from this final universal inequality. Finite computation is evidence and counterexample pressure, not a substitute for a universal proof.

### Twin-prime archival status

```text
TWIN_PRIME_RESEARCH_DIRECTION = SPATIAL LAW
TWIN_PRIME_CURRENT_PAPER = FINITE-BOUNDARY ADAPTIVE SHELLS AND EXACT MULTIPLICATIVE OCCUPANCY FOR TWIN-PRIME WINDOWS
TWIN_PRIME_CURRENT_DOI = 10.5281/zenodo.22888216
CONTINUOUS_ADMISSIBLE_SHELL = I_N = (3^N, 3^(N+1))
EXACT_WINDOW_IDENTITY = T_N = C_N - Q_N = C_N - U_N + D_N
UNIVERSAL_NON_FULL_COVERAGE_QN_LT_CN = PENDING
PREVIOUS_TWIN_PRIME_DOI = 10.5281/zenodo.22851583
EARLIER_TWIN_PRIME_ARCHIVE_DOI = 10.5281/zenodo.22701838
COMMUNITY_STATUS_OF_TWIN_PRIME_CONJECTURE = OPEN
```

See the dedicated [Twin Prime Research index](TWIN_PRIME_RESEARCH.md).

---

# III. Publications and archived papers

The full paper chronology is maintained in [`PUBLICATIONS.md`](PUBLICATIONS.md).

## Collatz sequence

1. Local control completeness — `10.5281/zenodo.22096604`
2. Four-mode global control completeness — `10.5281/zenodo.22104057`
3. Nonzero-integer global exact control — `10.5281/zenodo.22109060`
4. Fixed standard-map dyadic / threefold architecture — `10.5281/zenodo.22182820`
5. Exact finite valuation geometry — `10.5281/zenodo.22197750`
6. Rooted-generative complete-analysis formulation — `10.5281/zenodo.22246883`

## Independent number-theory branch

1. **Finite-Boundary Adaptive Shells and Exact Multiplicative Occupancy for Twin-Prime Windows** — `10.5281/zenodo.22888216`
   - Research direction: **Twin Prime Research (Spatial Law)**
   - Previous canonical record: *Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1* — `10.5281/zenodo.22851583`
   - Earlier archive: *A Complete Analysis of Twin Primes* — `10.5281/zenodo.22701838`

---

## General research guardrails

```text
EXACT_INTEGER_IDENTITIES > HEURISTIC INTERPRETATION
FINITE_AUDIT != SUBSTITUTE_FOR_SYMBOLIC_PROOF
PROJECT_THEOREM_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
