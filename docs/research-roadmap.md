# Research Roadmap

## Phase I — Local theorem freeze — COMPLETE

- W-MPOCCT on the fixed-multiplier \(\mu=3\), \(+1/+3\) selector system.
- Exact positive-integer domain.
- RESET / ESCAPE controlled policies.
- Fixed-selector loss-of-control principle.

Status:

```text
W-MPOCCT = PROVED / FROZEN
```

## Phase II — Four-mode global control — COMPLETE

For

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),\qquad (\mu,c)\in\{1,3\}^2,
\]

the following have been independently audited:

- exact closure;
- global reset to \(1\);
- five-case smaller-target-source lemma;
- strong-induction generation \(1\leadsto N\);
- global strong connectivity;
- universal target simple-cycle embedding;
- global escape control.

Status:

```text
FOUR_MODE_ODD_SYSTEM_GLOBAL_CONTROL = PROVED / FROZEN
```

## Phase III — Passive deterministic branch / universal outcome — CURRENT CORE OPEN PROGRAM

Fix both control coordinates:

\[
(\mu,c)=(3,1).
\]

Then the forward route is unique. The principal remaining question is not controllability, but outcome:

\[
\forall n\in\Omega,\ \exists k:\ T^k(n)=1\ ?
\]

This is exactly the classical Collatz conjecture.

Research directions include:

- structural comparison between the full four-mode control graph and the fixed passive branch;
- characterization of the residue-imposed UP/FOLD sequence;
- nontrivial fixed-branch cycle exclusion;
- exclusion of unbounded fixed-branch positive-integer orbits;
- identification of invariant or monotone information that survives removal of active control.

## Independent technical program — NOT REQUIRED for Phase II

The following remain mathematically meaningful but no longer block the global four-mode theorem:

- PLDT;
- MPD18;
- pure-\(F\) periodicity;
- pure-\(F\) cycle classification;
- \(\nu_3=2\) higher residue-cylinder analysis.

These should be pursued only when they contribute information about the fixed passive branch or independent arithmetic structure.

## Publication / prior-art track

- Maintain the local W-MPOCCT paper as a separate theorem note.
- Maintain the four-mode global-control paper as a separate theorem note.
- Keep theorem naming neutral until community/prior-art review supports stronger naming.
- Add DOI / archived-paper metadata only after publication records are finalized.

```text
GLOBAL_COLLATZ = OPEN
FOUR_MODE_GLOBAL_CONTROL != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
```
