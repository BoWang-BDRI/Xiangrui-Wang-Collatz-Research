# Xiangrui Wang — Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Xiangrui Wang** at the **Bipolar-Dynamics Research Institute (BDRI)**. The repository is centered on the Collatz research program and now also contains an independent number-theory branch on twin primes.

**Researcher:** Xiangrui Wang  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research areas:** Collatz-type dynamics, arithmetic dynamics, exact integer control, dyadic coordinates, inverse dynamics, prime-generation structure, twin primes  
**Contact:** xljun521521@gmail.com

---

## Quick navigation

| Research branch | Current record | DOI / files |
|---|---|---|
| **Collatz mathematics** | *A Complete Analysis of the Collatz Conjecture* project record | [10.5281/zenodo.22246883](https://doi.org/10.5281/zenodo.22246883) |
| **Twin prime research** | *Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1* (v2.0) | [10.5281/zenodo.22851583](https://doi.org/10.5281/zenodo.22851583) · [`twin-prime/`](twin-prime/) |
| **Publication index** | Archived research papers | [`PUBLICATIONS.md`](PUBLICATIONS.md) |

---

# I. Collatz Mathematics Research

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

# II. Twin Prime Research

## Current paper

### **Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1**

*Source Decomposition, Occupancy, and Exact Localization Between Consecutive Prime Squares*

- **Author:** Xiangrui Wang
- **Version:** v2.0
- **Date:** September 20, 2026
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22851583
- **Research directory:** [`twin-prime/`](twin-prime/)
- **Citation metadata:** [`twin-prime/CITATION.cff`](twin-prime/CITATION.cff)
- **Previous archived paper:** *A Complete Analysis of Twin Primes*, v1.4.2 — https://doi.org/10.5281/zenodo.22701838

### 1. Ordered odd-composite source trajectories

For every odd base \(a\ge3\),

\[
\boxed{G_a=\{a^2+2ak:k\in\mathbb Z_{\ge0}\}}.
\]

Their union is exactly the set of odd composite integers. Composite-base layers preserve factor-source provenance but contribute no new first-owned positions; the least-prime-factor skeleton activates at prime squares.

### 2. Exact twin-prime localization operator

For consecutive primes \(5\le p<q\), let \(\mathcal W(p,q)\) be the complete modulo-6 windows contained in \((p^2,q^2)\). Define

\[
\Theta(n)=
\prod_{\substack{r\in\mathbb P\\5\le r\le p}}
\left(1-\mathbf1_{r\mid(6n-1)}\right)
\left(1-\mathbf1_{r\mid(6n+1)}\right)
\]

on the band, and

\[
\boxed{L_{TS}(p,q)=\sum_{n\in\mathcal W(p,q)}\Theta(n)}.
\]

The exact-band localization theorem proves that \(L_{TS}(p,q)\) is exactly the number of actual twin-prime pairs wholly contained in \((p^2,q^2)\). It is an integer locator, not a density estimate.

### 3. Strongly bound core candidate theorems

The current paper treats the operator and the two candidate theorems as one load-bearing module:

\[
\boxed{C0:\ L_{TS}(p,q)\ge2}
\]

and

\[
\boxed{C1:\ L_{TS}(p,q)\ge q-p},
\]

for every consecutive prime pair \(5<p<q\). Since \(q-p\ge2\), \(C1\Rightarrow C0\). A complete analytic certification of C0 would immediately imply infinitely many twin-prime pairs because the consecutive prime-square bands are infinite in number and pairwise disjoint.

### 4. First-owner coverage, overlap, and exact equivalents

For each band, disjoint first-owner counting gives

\[
L_{TS}(p,q)=G(p,q)-F(p,q).
\]

Therefore the two core candidates are exactly equivalent to

\[
C0\iff F(p,q)\le G(p,q)-2,
\]

\[
C1\iff F(p,q)\le G(p,q)-(q-p).
\]

The paper also separates repeated source hits on the same endpoint from windows whose two endpoints are composite, preventing endpoint-level overcounting from being mistaken for destroyed-window count.

### 5. CRT locator and survivor thresholds

The paired residue system yields an exact CRT floor-sum representation of \(L_{TS}\), together with sharp cyclic quantities \(J_2(p)\) and \(D_2(p)\) controlling one- and two-survivor guarantees under arbitrary translation. These are exact structural tools; they are not substituted for the universal C0/C1 lower bounds.

### 6. Proof-status boundary

The structural identities, source completeness, exact localization, first-owner decomposition, overlap identities, and CRT formulas are proved within the manuscript. C0 and C1 are the two core candidate theorems undergoing independent certification of their universal analytic bounds.

A counterexample to C0 is a consecutive prime pair \(5<p<q\) with \(L_{TS}(p,q)<2\).  
A counterexample to C1 satisfies \(L_{TS}(p,q)<q-p\).

A gap in a submitted proof is not itself a numerical counterexample; it means the corresponding proof has not yet been certified.

### 7. Evidence and reproducibility

The current paper separates:
- reproducible finite submission evidence;
- larger internal exact-stress records;
- universal analytic proof obligations.

Finite computation is used for implementation checks and counterexample search, not as a replacement for a universal proof. The existing public audit scripts remain in [`twin-prime/code/`](twin-prime/code/); they originated in the earlier v1.4.x package and are retained as historical reproducibility material unless a newer code package is explicitly archived.

### Twin-prime archival status

```text
TWIN_PRIME_CURRENT_PAPER = TWIN-PRIME GENERATION COMPLETENESS: STRONG EXACT LOCALIZATION OPERATOR AND CORE CANDIDATE THEOREMS C0/C1
CURRENT_VERSION = v2.0
ZENODO_DOI = 10.5281/zenodo.22851583
EXACT_LOCALIZATION_OPERATOR = L_TS
CORE_CANDIDATE_THEOREMS = C0 + C1
C1_IMPLIES_C0 = YES
C0_IMPLIES_TWIN_PRIME_INFINITUDE = CONDITIONAL_ON_ANALYTIC_CERTIFICATION
UNIVERSAL_C0_C1_CERTIFICATION = PENDING
PREVIOUS_ARCHIVE_DOI = 10.5281/zenodo.22701838
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

1. **Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1** — `10.5281/zenodo.22851583`
   - Previous archive: *A Complete Analysis of Twin Primes* — `10.5281/zenodo.22701838`

---

## General research guardrails

```text
EXACT_INTEGER_IDENTITIES > HEURISTIC INTERPRETATION
FINITE_AUDIT != SUBSTITUTE_FOR_SYMBOLIC_PROOF
PROJECT_THEOREM_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
