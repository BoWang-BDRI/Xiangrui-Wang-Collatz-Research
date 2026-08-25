# W-MPOCCT Theorem Overview

## Domain

Let \(\Omega=\mathbb N_{\mathrm{odd}}^+\), and for \(c\in\{1,3\}\) define

\[
U_c(n)=\operatorname{oddpart}(3n+c)
=\frac{3n+c}{2^{\nu_2(3n+c)}}.
\]

All statements below concern positive integers and positive odd accelerated states only.

## Wang Minimal Positive Odd-Pair Complete Control Theorem

**W-MPOCCT — 王氏最小正奇数对完备控制定理.** For every \(n\in\Omega\), the selector pair \(c\in\{1,3\}\) supplies exactly one shallow gate with dyadic valuation \(1\) and one folding gate with dyadic valuation at least \(2\). For \(n>3\), these gates respectively increase and decrease the current odd state. Their exact images partition \(\Omega\) according to divisibility by \(3\).

“Complete” means local control-option completeness only. It does not mean global reachability or strong connectivity.

## Exact proof components

### 1. Valuation complementarity

If \(n\equiv1\pmod4\), then \(3n+1\equiv0\pmod4\) and \(3n+3\equiv2\pmod4\). If \(n\equiv3\pmod4\), the roles reverse. Therefore

\[
\{\nu_2(3n+1),\nu_2(3n+3)\}=\{1,b(n)\},\qquad b(n)\ge2.
\]

### 2. Local height polarity

At valuation \(1\), \(U_c(n)=(3n+c)/2>n\). At valuation at least \(2\),

\[
U_c(n)\le\frac{3n+3}{4}<n
\]

for \(n>3\).

### 3. Exact image partition

Since \(3n+1\not\equiv0\pmod3\), division by a power of \(2\) keeps \(U_1(n)\) outside the \(3\)-multiples. Conversely, for each odd \(m\) not divisible by \(3\), choose \(a\ge1\) with \(2^a m\equiv1\pmod3\); then \(n=(2^a m-1)/3\) is positive odd and \(U_1(n)=m\).

Similarly, every \(U_3(n)\) is divisible by \(3\). Conversely, if \(m=3r\) is positive odd, then \(n=2r-1\) is positive odd and \(U_3(n)=m\). Thus

\[
\operatorname{Im}(U_1)=\{m\in\Omega:3\nmid m\},
\qquad
\operatorname{Im}(U_3)=\{m\in\Omega:3\mid m\}.
\]

### 4. Controlled RESET and ESCAPE

For RESET, choose the folding gate while \(n>3\); strict descent on positive odd integers reaches \(\{1,3\}\) in finitely many steps. The stated terminal convention sends \(1\) to \(3\) and fixes \(3\). For ESCAPE, choose the shallow gate at each state; the resulting recurrence is strictly increasing beyond \(1\) and grows without bound.

## Fixed-policy boundary

The accelerated classical Collatz map fixes \(c=1\). It therefore has no active selector choice, and W-MPOCCT does not prove that its residue-imposed trajectory always chooses enough folding gates. The classical Collatz conjecture remains open.

```text
GLOBAL_COLLATZ = OPEN
LOCAL_CONTROL_COMPLETENESS != GLOBAL_STRONG_CONNECTIVITY
```

