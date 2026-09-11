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

- `paper/README.md` — paper title, abstract, version, and canonical Zenodo DOI.
- `code/exact_integer_audit_v1_4.py` — exact finite regression audit.
- `code/counterexample_condition_audit_v1_4.py` — exact counterexample-condition audit.
- `CITATION.cff` — citation metadata for the Zenodo paper.

The full manuscript PDF and complete v1.4.2 research package are archived under the Zenodo DOI above.

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

This directory preserves the public research index and reproducibility code corresponding to the Zenodo DOI above. Journal submission and peer review are separate from the archival record.
