# Twin Prime Research — Spatial Law

**Author:** Xiangrui Wang  
**Research program:** Independent Number Theory Research  
**Current direction:** **Spatial Law**  
**Date:** September 22, 2026  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22888216

## Current paper

**Finite-Boundary Adaptive Shells and Exact Multiplicative Occupancy for Twin-Prime Windows**

The current paper studies twin-prime windows through the continuous admissible shell chain

\[
I_N=(3^N,3^{N+1}),\qquad N\ge2.
\]

All predecessor odd integers below the left boundary are retained as sources. Their actual odd products are projected into the current shell, deduplicated by landing position, and only then classified as composite occupancy, prime residuals, and twin-prime windows.

The shell capacity is

\[
C_N=3^{N-1},
\]

and the exact twin-window count is

\[
\boxed{T_N=C_N-Q_N=C_N-U_N+D_N}.
\]

The normalized entry law

\[
1<\frac{a}{A_N}b<3
\]

has the same form at every scale, while

\[
a\ge A_N,\ b\ge3
\Longrightarrow
ab\ge3A_N
\]

gives the no-retroactive-fill property: completed shells are permanent.

The final universal load-bearing condition is

\[
\boxed{Q_N<C_N}.
\]

It is kept explicit rather than hidden inside a definition. Finite computation and exact identities are not substituted for a universal proof.

## Research roadmap

- [`RESEARCH_ROADMAP.md`](RESEARCH_ROADMAP.md) — chronological route from bottom-level occupancy through prime-square localization to the current finite-boundary adaptive shell framework.

## Repository contents

- `paper/README.md` — current paper metadata and abstract.
- `CITATION.cff` — current citation metadata.
- `code/exact_integer_audit_v1_4.py` — historical exact finite regression audit.
- `code/counterexample_condition_audit_v1_4.py` — historical counterexample-condition audit.

## Previous records

**Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1**, v2.0  
DOI: https://doi.org/10.5281/zenodo.22851583

**A Complete Analysis of Twin Primes**, v1.4.2  
DOI: https://doi.org/10.5281/zenodo.22701838

## Citation

Please cite the current Zenodo record:

> Wang, Xiangrui. *Finite-Boundary Adaptive Shells and Exact Multiplicative Occupancy for Twin-Prime Windows*. Zenodo, 2026. DOI: 10.5281/zenodo.22888216.

## Status

The current DOI is the canonical archived record of the Spatial Law shell framework. Journal submission and independent peer review are separate from the Zenodo archive. The classical twin-prime conjecture remains open in the mathematical community pending independent acceptance of any proposed proof.

