# Twin Prime Research

This repository includes an independent number-theory research branch on twin primes, separate from the Collatz program.

## Current paper

**Twin-Prime Generation Completeness: Strong Exact Localization Operator and Core Candidate Theorems C0/C1**  
*Source Decomposition, Occupancy, and Exact Localization Between Consecutive Prime Squares*  
**Author:** Xiangrui Wang  
**Version:** v2.0  
**Date:** September 20, 2026  
**Zenodo DOI:** https://doi.org/10.5281/zenodo.22851583

Research directory: [`twin-prime/`](twin-prime/)  
Research roadmap: [`twin-prime/RESEARCH_ROADMAP.md`](twin-prime/RESEARCH_ROADMAP.md)

Previous archive: **A Complete Analysis of Twin Primes**, v1.4.2 — https://doi.org/10.5281/zenodo.22701838

## Core architecture

The current manuscript retains the source-resolved odd-composite trajectories

\[
G_a=\{a^2+2ak:k\ge0\},
\]

the modulo-6 twin window

\[
W_n=(6n-1,6n+1),
\]

prime-square activation, completed-prefix invariance, and finite-front source completeness.

For each consecutive prime-square band \((p^2,q^2)\), the strong exact localization operator

\[
L_{TS}(p,q)
\]

is proved to equal the actual number of twin-prime pairs wholly contained in the band.

## Core candidate-theorem module

The operator is strongly bound to two coequal core candidate theorems:

\[
C0:\quad L_{TS}(p,q)\ge2,
\]

\[
C1:\quad L_{TS}(p,q)\ge q-p,
\]

for every pair of consecutive primes \(5<p<q\).

Since \(q-p\ge2\),

\[
C1\Rightarrow C0.
\]

A complete analytic certification of C0 implies infinitely many twin-prime pairs.

The exact first-owner identity

\[
L_{TS}(p,q)=G(p,q)-F(p,q)
\]

turns the two candidates into explicit exact coverage bounds:

\[
C0\iff F(p,q)\le G(p,q)-2,
\]

\[
C1\iff F(p,q)\le G(p,q)-(q-p).
\]

The paper further contains source-overlap identities, endpoint-to-window correction, activation-band first-owner structure, an exact CRT floor-sum locator, and sharp cyclic one-/two-survivor thresholds.

## Review boundary

The exact structural framework and localization operator are separated from the universal analytic lower bounds. Finite computation is evidence and counterexample pressure, not a substitute for universal proof.

A hard C0 counterexample is a consecutive prime pair \(5<p<q\) with \(L_{TS}(p,q)<2\).  
A hard C1 counterexample has \(L_{TS}(p,q)<q-p\).

The current DOI above is the canonical archived paper record for v2.0.

## Repository material

- [`twin-prime/README.md`](twin-prime/README.md) — current research summary.
- [`twin-prime/paper/README.md`](twin-prime/paper/README.md) — paper metadata and abstract.
- [`twin-prime/CITATION.cff`](twin-prime/CITATION.cff) — current citation metadata.
- [`twin-prime/code/`](twin-prime/code/) — existing public exact-integer audit scripts retained from the earlier research package.

