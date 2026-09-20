# Twin Prime Research — Strong Exact Localization and Core Candidate Theorems C0/C1

**Author:** Xiangrui Wang  
**Research program:** Independent Number Theory Research  
**Version:** v2.0 (September 20, 2026)  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22851583

## Current paper

**Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1**

*Source Decomposition, Occupancy, and Exact Localization Between Consecutive Prime Squares*

The paper develops a source-preserving exact integer framework based on the fixed odd-product trajectories

\[
G_a=\{a^2+2ak:k\ge0\}.
\]

Their union is exactly the odd composites, while the modulo-6 windows

\[
W_n=(6n-1,6n+1)
\]

give the unique ordinary twin-prime windows.

For consecutive primes \(5\le p<q\), the manuscript defines the strong exact localization operator

\[
L_{TS}(p,q),
\]

and proves that it equals exactly the number of actual twin-prime pairs wholly contained in \((p^2,q^2)\).

## Core candidate-theorem module

The current paper binds the exact locator to two coequal candidate theorems:

\[
C0:\quad L_{TS}(p,q)\ge2,
\]

\[
C1:\quad L_{TS}(p,q)\ge q-p,
\]

for all consecutive primes \(5<p<q\).

The first-owner identity

\[
L_{TS}(p,q)=G(p,q)-F(p,q)
\]

gives the exact equivalents

\[
C0\iff F(p,q)\le G(p,q)-2,
\]

\[
C1\iff F(p,q)\le G(p,q)-(q-p).
\]

The paper also contains exact first-owner counting, endpoint-to-window overlap correction, activation-band first-owned structure, CRT floor-sum localization, and cyclic one-/two-survivor thresholds.

## Logical status

\[
C1\Rightarrow C0.
\]

A complete analytic certification of C0 implies infinitely many twin-prime pairs.

The manuscript deliberately separates exact structural theorems, the exact locator, candidate-theorem certification, finite evidence, and universal analytic proof obligations.

## Research roadmap

- [`RESEARCH_ROADMAP.md`](RESEARCH_ROADMAP.md) — consolidated route from the 2026-09-07 bottom-level occupancy baseline through corridor/paired-wheel audits to the current `L_TS + C0 + C1` architecture.

## Repository contents

- `paper/README.md` — current paper metadata and abstract.
- `CITATION.cff` — current citation metadata.
- `code/exact_integer_audit_v1_4.py` — historical exact finite regression audit from the earlier package.
- `code/counterexample_condition_audit_v1_4.py` — historical counterexample-condition audit from the earlier package.

## Previous archive

The preceding archived paper was:

**A Complete Analysis of Twin Primes**, v1.4.2  
DOI: https://doi.org/10.5281/zenodo.22701838

## Citation

Please cite the current Zenodo record:

> Wang, Xiangrui. *Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1*. Zenodo, 2026. DOI: 10.5281/zenodo.22851583.

## Status

The current DOI is the canonical archived v2.0 paper record. Journal submission and independent peer review are separate from the Zenodo archive. The classical twin-prime conjecture remains open in the mathematical community pending independent acceptance of any proposed proof.
