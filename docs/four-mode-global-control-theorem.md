# Four-Mode Odd-System Global Control Completeness Theorem

## Status

```text
FOUR_MODE_ODD_SYSTEM_GLOBAL_CONTROL = PROVED / FROZEN
GLOBAL_COLLATZ = OPEN
```

This document concerns only positive integers, with accelerated states restricted to

\[
\Omega=\mathbb N_{\mathrm{odd}}^{+}.
\]

## Four exact control modes

Define

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c)
=\frac{\mu n+c}{2^{\nu_2(\mu n+c)}},
\qquad (\mu,c)\in\{1,3\}\times\{1,3\}.
\]

The four modes are

\[
(1,1),\ (1,3),\ (3,1),\ (3,3).
\]

The dyadic exponent is always the exact valuation of the chosen positive integer \(\mu n+c\). It is not a free parameter.

## Theorem

In this four-mode positive-odd system:

1. every state reaches \(1\);
2. \(1\) reaches every state;
3. every ordered pair of states is mutually reachable;
4. every positive odd state lies on a finite nontrivial exact directed cycle;
5. every positive odd state admits an exact escaping control trajectory.

## 1. Global reset

Use only the mode \((1,1)\):

\[
R(n)=V_{1,1}(n)=\operatorname{oddpart}(n+1).
\]

For every odd \(n>1\),

\[
R(n)\le\frac{n+1}{2}\le\frac23n<n.
\]

Hence repeated \((1,1)\) reaches \(1\) in finitely many steps.

## 2. Smaller exact source for every target

For every positive odd target \(N>1\), there exists a positive odd source

\[
p<\frac89N
\]

that reaches \(N\) in at most three exact control steps.

The exhaustive cases are:

| Target class | Smaller source \(p\) | Exact control word |
|---|---:|---|
| \(N\equiv2\pmod3\) | \((2N-1)/3\) | \((3,1)\) |
| \(N\equiv0\pmod3\) | \((2N-3)/3\) | \((3,3)\) |
| \(N\equiv4\pmod9\) | \((8N-5)/9\) | \((3,1),(3,1)\) |
| \(N\equiv7\pmod9\) | \((8N-11)/9\) | \((3,3),(3,1)\) |
| \(N\equiv1\pmod{18},\ N>1\) | \((8N-17)/9\) | \((3,1),(3,1),(1,3)\) |

For the last case, writing \(N=18s+1\), define

\[
p=16s-1,\quad q=24s-1,\quad r=36s-1.
\]

Then

\[
3p+1=2q,\qquad 3q+1=2r,\qquad r+3=2N,
\]

so all three valuations are exactly \(1\).

## 3. Global generation

Strong induction on the target gives

\[
1\leadsto N\qquad\forall N\in\Omega.
\]

The recursive source is always strictly smaller than the target, so the induction is well-founded.

A crude constructive bound is

\[
L_{\mathrm{target}}(1,N)\le3\left\lceil\log_{9/8}N\right\rceil.
\]

## 4. Global strong connectivity

Since every \(x\) reaches \(1\) and \(1\) reaches every \(y\),

\[
\forall x,y\in\Omega,\qquad x\leadsto1\leadsto y.
\]

Thus the exact four-mode directed control graph is strongly connected.

## 5. Universal exact cycle embedding

For \(N>1\), concatenate

\[
N\leadsto1\leadsto N.
\]

A shortest positive-length closed walk based at \(N\) is a simple directed cycle containing \(N\).

For \(N=1\), an explicit nontrivial cycle is

\[
1\xrightarrow{(3,3)}3\xrightarrow{(1,1)}1.
\]

No uniqueness of the cycle is claimed.

## 6. Global escape

For every positive odd \(n\), exactly one of \(3n+1\) and \(3n+3\) is congruent to \(2\pmod4\). Choose the corresponding selector \(c\). Then

\[
\nu_2(3n+c)=1,
\qquad
V_{3,c}(n)=\frac{3n+c}{2}>\frac32n.
\]

Repeating this state-dependent shallow choice produces divergence to \(+\infty\).

## 7. Standard Collatz is a fixed passive branch

The standard accelerated Collatz map is

\[
T(n)=V_{3,1}(n)=\operatorname{oddpart}(3n+1).
\]

Here both controls are fixed:

\[
\mu\equiv3,\qquad c\equiv1.
\]

Therefore the forward route from each starting state is unique. This is definitional determinism.

The open question is whether the unique passive route always has terminal outcome \(1\):

\[
\forall n\in\Omega,\ \exists k\ge0:\ T^k(n)=1\ ?
\]

This is exactly the classical Collatz conjecture.

```text
PASSIVE_FORWARD_ROUTE_UNIQUENESS = DEFINITIONAL
UNIVERSAL_PASSIVE_OUTCOME = 1 = COLLATZ / OPEN
FOUR_MODE_GLOBAL_CONTROL != STANDARD_COLLATZ_PROOF
```

## Prior-art boundary

The theorem has been independently red-team audited. No direct prior art for this exact four-mode global-control formulation was found in that audit. Structurally related generalized Collatz maps, semigroup formulations, and +1/+3 branching discussions exist; therefore novelty is stated conservatively.
