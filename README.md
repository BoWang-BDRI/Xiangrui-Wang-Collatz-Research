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
| **Twin prime research** | *A Complete Analysis of Twin Primes* | [10.5281/zenodo.22701838](https://doi.org/10.5281/zenodo.22701838) · [`twin-prime/`](twin-prime/) |
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

### **A Complete Analysis of Twin Primes**

- **Author:** Xiangrui Wang
- **Version:** v1.4.2
- **Date:** September 11, 2026
- **Zenodo DOI:** https://doi.org/10.5281/zenodo.22701838
- **Research directory:** [`twin-prime/`](twin-prime/)
- **Citation metadata:** [`twin-prime/CITATION.cff`](twin-prime/CITATION.cff)

### 1. Canonical odd-composite trajectories

For odd \(a\ge3\) and \(k\in\mathbb N_0\),

\[
\boxed{G_a(k)=a(a+2k)=a^2+2ak}.
\]

The framework treats odd composites through exact source-preserving trajectories and proves the divisor-track embedding relation. At Boolean occupancy level, composite-base tracks reduce to the prime skeleton.

### 2. Prime-square activation and finite-stage certification

For a prime base \(p\), the independent prime track activates at \(p^2\). Consecutive prime-square shells provide finite certification regions whose already-certified states remain stable as later tracks activate.

The active support of an internal odd position is

\[
A(x)=\{p\ge5:p\text{ prime},\ p\mid x,\ p^2\le x\},
\qquad
m(x)=|A(x)|.
\]

For internal positions \(x\equiv\pm1\pmod6\),

\[
\boxed{m(x)=0\iff x\text{ is prime}}.
\]

### 3. Three-boundary window geometry

The standard window is

\[
W_n=(6n-1,6n+1).
\]

For each prime \(p\ge5\), the raw prime-track residues follow an exact modulo-6 period, and after the \(3\)-boundary hits are removed the internal hit gaps alternate between

\[
\boxed{2p\quad\text{and}\quad4p}.
\]

The exact window divisibility classes satisfy

\[
p\mid(6n-1)\iff n\equiv6^{-1}\pmod p,
\]

\[
p\mid(6n+1)\iff n\equiv-6^{-1}\pmod p.
\]

Once the relevant endpoint is at least \(p^2\), these divisibility classes are the active interruption classes of \(G_p\).

### 4. Exact finite twin-prime certifier

For

\[
P_n=\{p\ge5:p\text{ prime},\ p^2\le6n+1\},
\]

define

\[
\boxed{
T_{\rm fin}(n)=
\prod_{p\in P_n}
\left(1-\mathbf1_{p\mid(6n-1)}\right)
\left(1-\mathbf1_{p\mid(6n+1)}\right).
}
\]

The paper proves

\[
\boxed{T_{\rm fin}(n)=1\iff(6n-1,6n+1)\text{ is an ordinary twin-prime pair}}.
\]

The exceptional initial pair \((3,5)\) is handled separately.

### 5. Unbounded finite-certification domain

With finite stages \(D_b\), the manuscript proves

\[
D_3\subsetneq D_5\subsetneq D_7\subsetneq\cdots,
\qquad
\boxed{\bigcup_bD_b=\mathbb O}.
\]

Thus the same exact finite-certification rules extend without a finite upper boundary over the positive odd integers.

### 6. Quantified twin-prime infinitude equivalence

Let

\[
\mathcal T=\{n\in\mathbb N:T_{\rm fin}(n)=1\},
\]

and let \(N_{\rm twin}(X)\) be the cumulative number of twin-prime pairs up to \(X\). The final manuscript proves the formal equivalence

\[
\boxed{
|\mathcal T|=\infty
\iff
\forall M\in\mathbb N\;\exists n>M:T_{\rm fin}(n)=1
\iff
N_{\rm twin}(X)\text{ is unbounded}
\iff
\lim_{X\to\infty}N_{\rm twin}(X)=\infty.
}
\]

### 7. Reproducibility

Public exact-integer audit scripts:

- [`exact_integer_audit_v1_4.py`](twin-prime/code/exact_integer_audit_v1_4.py)
- [`counterexample_condition_audit_v1_4.py`](twin-prime/code/counterexample_condition_audit_v1_4.py)

Recorded final-package audit totals:

```text
PRIMARY EXACT-INTEGER AUDIT
ASSERTIONS = 12,611,102
VERDICT = PASS

COUNTEREXAMPLE-CONDITION AUDIT
AUDITED_CASES = 12,303,777
IN_DOMAIN_COUNTEREXAMPLES_P1_P7 = NONE
VERDICT = PASS
```

The computations are independent finite audits of the symbolic formulas; they are not substituted for the manuscript's exact integer derivations.

### Twin-prime archival status

```text
TWIN_PRIME_PAPER = A COMPLETE ANALYSIS OF TWIN PRIMES
FINAL_ARCHIVED_VERSION = v1.4.2
ZENODO_DOI = 10.5281/zenodo.22701838
PUBLIC_REPRODUCIBILITY_CODE = AVAILABLE
JOURNAL_SUBMISSION = SEPARATE FROM ZENODO ARCHIVE
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

1. **A Complete Analysis of Twin Primes** — `10.5281/zenodo.22701838`

---

## General research guardrails

```text
EXACT_INTEGER_IDENTITIES > HEURISTIC INTERPRETATION
FINITE_AUDIT != SUBSTITUTE_FOR_SYMBOLIC_PROOF
PROJECT_THEOREM_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
