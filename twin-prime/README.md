# Twin Prime Research — A Complete Analysis of Twin Primes

**Author:** Xiangrui Wang  
**Research program:** Independent Number Theory Research  
**Version:** v1.4.2 (September 11, 2026)  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22701838

## Paper

**A Complete Analysis of Twin Primes**

The paper develops an exact integer framework for odd-composite occupancy using

\[
G_a(k)=a(a+2k)=a^2+2ak,
\]

reduces Boolean occupancy to prime-base tracks, and derives prime-square activation, odd square-shell closure, modulo-6 window geometry, active-support classification, exact finite track intersections, finite-stage certification, and permanent stability of certified regions.

For each ordinary twin-prime window \((6n-1,6n+1)\), the paper defines a finite exact certifier \(T_{\rm fin}(n)\) over the active primes and proves that \(T_{\rm fin}(n)=1\) exactly for an ordinary twin-prime pair.

Writing \(\mathcal T=\{n\in\mathbb N:T_{\rm fin}(n)=1\}\) and \(N_{\rm twin}(X)\) for the cumulative twin-pair count, the manuscript proves the formal equivalence

\[
|\mathcal T|=\infty
\iff
\forall M\in\mathbb N\;\exists n>M:T_{\rm fin}(n)=1
\iff
N_{\rm twin}(X)\text{ is unbounded}
\iff
\lim_{X\to\infty}N_{\rm twin}(X)=\infty.
\]

## Repository contents

- `paper/` — final manuscript sources and bibliography.
- `code/` — exact-integer finite regression and counterexample-condition audit scripts.
- `supplement/` — computational audit, provenance, and AI/LLM disclosure.

## Reproducibility

The computational material is an independent finite audit of the symbolic formulas. It is not used as a substitute for the paper's exact integer arguments.

Primary audit recorded in the final package:

```text
ASSERTIONS=12611102
VERDICT=PASS
```

Counterexample-condition audit recorded in the final package:

```text
AUDITED_CASES=12303777
IN_DOMAIN_COUNTEREXAMPLES_P1_P7=NONE
VERDICT=PASS
```

## Citation

Please cite the archived Zenodo record:

> Wang, Xiangrui. *A Complete Analysis of Twin Primes*. Zenodo, 2026. DOI: 10.5281/zenodo.22701838.

## Status

This directory preserves the public research record corresponding to the Zenodo DOI above. Journal submission and peer review are separate from the archival record.
