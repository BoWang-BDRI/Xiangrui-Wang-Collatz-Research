# Xiangrui Wang — Collatz Mathematics Research

### Bipolar-Dynamics Research Institute (BDRI)

This repository is the public mathematical research index for **Collatz-type discrete dynamics** led by **Xiangrui Wang**, Researcher at the **Bipolar-Dynamics Research Institute (BDRI)**.

**Researcher:** Xiangrui Wang  
**Institution:** Bipolar-Dynamics Research Institute (BDRI)  
**Research area:** Collatz-type dynamics, discrete arithmetic systems, residue dynamics, dyadic normalization  
**Contact:** xljun521521@gmail.com

## Scope and core research object

Let

\[
\Omega=\mathbb N_{\mathrm{odd}}^{+}.
\]

For \(c\in\{1,3\}\), define the accelerated selector maps

\[
U_c(n)=\operatorname{oddpart}(3n+c)
=\frac{3n+c}{2^{\nu_2(3n+c)}}.
\]

All dynamical theorem statements in this repository are restricted to positive integers and positive odd accelerated states. Negative, rational, real, and p-adic extensions are outside the theorem domain.

## Main proved theorem

### Wang Minimal Positive Odd-Pair Complete Control Theorem (W-MPOCCT)

### 王氏最小正奇数对完备控制定理

The minimal positive odd pair \(\{1,3\}\) appears in two coupled roles:

1. the multiplicative baseline / upper layer \(1N,3N\);
2. the additive selector pair \(+1,+3\).

Across the two selectors, exact dyadic normalization gives one shallow gate with valuation \(1\), one folding gate with valuation at least \(2\), both local height signs, and a full odd-output partition by divisibility by \(3\).

> “Complete” means local control-option completeness only. It does not mean global reachability or strong connectivity.

A proof-focused summary is provided in [the theorem overview](docs/theorem-overview.md).

## Frozen proved structure

### Dyadic threshold

\[
2<3<4,
\qquad
\frac32>1>\frac34.
\]

### Selector valuation complementarity

For every positive odd \(n\),

\[
\{\nu_2(3n+1),\nu_2(3n+3)\}
=\{1,b(n)\},
\qquad b(n)\ge2.
\]

### Odd-image partition

Define

\[
S_{\not3}=\{m\in\Omega:3\nmid m\},
\qquad
S_3=\{m\in\Omega:3\mid m\}.
\]

Then

\[
\operatorname{Im}(U_1)=S_{\not3},
\qquad
\operatorname{Im}(U_3)=S_3,
\]

and therefore

\[
S_{\not3}\cap S_3=\varnothing,
\qquad
S_{\not3}\sqcup S_3=\Omega.
\]

### Local height polarity

For \(n>3\),

\[
\nu_2(3n+c)=1\Rightarrow U_c(n)>n,
\]

whereas

\[
\nu_2(3n+c)\ge2\Rightarrow U_c(n)<n.
\]

### RESET and ESCAPE

- **RESET:** while \(n>3\), repeatedly choose the folding selector. Strict descent reaches \(\{1,3\}\) in finitely many steps. Under the terminal convention \(U_3(1)=3\) and \(U_3(3)=3\), the terminal state is \(3\).
- **ESCAPE:** repeatedly choosing the shallow selector produces a strictly increasing orbit (after the possible initial state \(1\)) and divergence to \(+\infty\).

### Fixed-selector loss of control

The standard accelerated Collatz map is the fixed policy \(c_k\equiv1\). Fixing the selector removes active local choice between shallow and folding gates; the UP/FOLD sequence is imposed by residue evolution. This observation does **not** imply global convergence.

On the positive odd \(3\)-multiple sheet, multiplication by \(3\) gives the exact conjugacy

\[
U_3(3n)=3U_1(n).
\]

## Current technical frontier

Define the pure minimum-port map

\[
F(3k)=4k,
\qquad
F(3k+1)=2k,
\qquad
F(3k+2)=2k+1,
\]

or equivalently

\[
F(m)=2^{\mathbf 1_{3\mid m}}\left\lfloor\frac{2m}{3}\right\rfloor.
\]

The currently frozen reductions are only:

- \(m\not\equiv0\pmod3\): one-step descent;
- \(\nu_3(m)=1\): two-step descent;
- for \(m=9u\), \(u\bmod9\in\{1,5,7,8\}\Rightarrow F^4(m)<m\).

The first unresolved mod-9 cylinders are \(u\equiv2,4\pmod9\). No mod-27, mod-81, or mod-243 dangerous list is frozen as proved.

The exact minimum-port cycle

\[
18\to24\to32\to21\to28\to18
\]

is a finite symbolic certificate. It does not establish uniqueness. A legal two-lift port repair sends the exceptional minimum start \(18\) to \(17\):

```text
M18_TWO_LIFT_DESCENT = PROVED
```

## Open conjectures

The following are all **OPEN**:

1. Fixed-\(+1\) Global Reset (equivalent to the classical Collatz conjecture).
2. Fixed-\(+3\) Global Reset (equivalent through the \(\times3\) conjugacy on the \(3\)-multiple odd sheet).
3. Wang Global Control Completeness Conjecture.
4. Universal Target Simple-Cycle Embedding.
5. 3-Anchored Simple-Cycle Embedding (stronger than item 4).
6. Port-Lift Descent (PLDT).
7. Minimum-Port Descent Except 18 (MPD18).
8. Non-descending periodicity of the pure minimum-port map.
9. Full classification of pure minimum-port cycles.

See [open problems](docs/open-problems.md), the [research roadmap](docs/research-roadmap.md), [research status](RESEARCH_STATUS.md), and the [public claims boundary](PUBLIC_CLAIMS_BOUNDARY.md).

## Absolute mathematical guardrails

```text
DOMAIN = POSITIVE_INTEGERS_ONLY
ODD_STATE_DOMAIN = N_ODD_POSITIVE
NEGATIVE_RATIONAL_REAL_PADIC_OBJECTS = OUTSIDE_THEOREM_DOMAIN

GLOBAL_COLLATZ = OPEN
MIXED_PLUS1_PLUS3_CONTROL_SYSTEM != STANDARD_COLLATZ_SINGLE_PLUS1_BRANCH
MIXED_CYCLE != STANDARD_COLLATZ_COUNTEREXAMPLE
LOCAL_CONTROL_COMPLETENESS != GLOBAL_STRONG_CONNECTIVITY
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```

