# Wang Nonzero Integer Global Exact Control Theorem (W-NIGECT)

## Status

```text
W_NIGECT = PROVED / FROZEN
NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN
GLOBAL_COLLATZ = OPEN
```

## Formal domains

Active control domain:

\[
\mathcal D_{\mathrm{active}}=\mathbb Z\setminus\{0\}.
\]

Exact target domain:

\[
\mathcal T=\mathbb Z.
\]

Zero is a valid terminal target, but not an active control state. No transition is defined from zero.

## Microdynamics

### Nonzero odd states

Allow

\[
A_{\mu,c}(n)=\mu n+c,
\qquad
\mu\in\{1,3\},
\quad
c\in\{-3,-1,1,3\}.
\]

The affine output is even. If it is nonzero, the trajectory may continue through forced halving. If it is zero, the step is a legal terminal edge and the trajectory ends.

### Nonzero even states

Apply the deterministic transition

\[
H(m)=\frac m2.
\]

A finite path may terminate at any visited target vertex, including an even target.

## Micro/macro relation

For nonzero affine output,

\[
F_{\mu,c}(n)=\operatorname{sodd}(\mu n+c)
\]

is the compression of one affine step followed by exactly \(\nu_2(|\mu n+c|)\) forced halvings.

## Sign-reflection conjugacy

Let \(S(n)=-n\). Then

\[
S\circ A_{\mu,c}=A_{\mu,-c}\circ S,
\]

and

\[
S\circ H=H\circ S.
\]

Thus positive and negative microdynamics are sign-conjugate. This is not time reversal.

## Signed odd global control

The positive four-mode theorem supplies global control on positive odd integers. Sign conjugacy gives the negative mirror. The bridges

\[
1\to-2\to-1,
\qquad
-1\to2\to1
\]

join the two odd half-axes. Therefore all nonzero odd integers are mutually reachable.

## Exact even targeting

For any nonzero even target \(Y\), let

\[
\sigma=\operatorname{sgn}(Y),
\qquad
p=Y-\sigma.
\]

Then \(p\) is nonzero odd and

\[
A_{1,\sigma}(p)=Y.
\]

Hence every nonzero even integer is an exact internal target.

## Exact dyadic-position targeting

For any nonzero integer \(Y\) and admissible \(h\), define

\[
p_{Y,h}=2^hY-\operatorname{sgn}(Y).
\]

Then

\[
A_{1,\operatorname{sgn}(Y)}(p_{Y,h})=2^hY,
\]

and the forced halving chain reaches \(Y\) exactly \(h\) halving steps later.

## Main theorem

For every

\[
X,Y\in\mathbb Z\setminus\{0\},
\]

there exists a finite legal trajectory

\[
X\leadsto Y.
\]

Constructively:

1. force-halve \(X\) to its signed odd core;
2. use signed odd global control to reach \(Y\) if \(Y\) is odd;
3. if \(Y\) is even, reach \(Y-\operatorname{sgn}(Y)\) and apply one affine step to land exactly at \(Y\).

Thus the active nonzero-integer micrograph is globally strongly connected.

## Wang All-Integer Exact Targetability Corollary

For every nonzero source \(X\) and every integer target \(Y\), including \(0\),

\[
X\leadsto Y.
\]

If \(Y=0\), first control to \(1\), then take the legal terminal edge

\[
1\xrightarrow{A_{1,-1}}0.
\]

The trajectory terminates at zero.

This is targetability, not strong connectivity of all of \(\mathbb Z\).

## Further consequences

- every nonzero integer lies on a finite nontrivial simple directed controlled cycle;
- every nonzero integer admits a controlled trajectory to \(+\infty\);
- every nonzero integer admits a controlled trajectory to \(-\infty\).

## Archived papers

### English

**Global Exact Controllability of the Nonzero-Integer Microdynamics under Signed Affine Controls and Forced Halving**  
https://doi.org/10.5281/zenodo.22109060

### 中文

**《带符号仿射控制与强制二分下非零整数微动力的全局精确可控性》**  
https://doi.org/10.5281/zenodo.22108987

## Classical Collatz boundary

Standard Collatz fixes the positive policy \((\mu,c)=(3,1)\) at odd states and uses forced halving at even states. W-NIGECT allows additional active controls, so it is a theorem about a larger controlled parent graph.

```text
GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
```
