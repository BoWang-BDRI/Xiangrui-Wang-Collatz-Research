# Research Roadmap

## Phase I — Local theorem freeze — COMPLETE

- W-MPOCCT on the fixed-multiplier \(\mu=3\), \(+1/+3\) selector system.
- Local control-option completeness.
- RESET / ESCAPE controlled policies.

```text
W-MPOCCT = PROVED / FROZEN
```

Archived paper: https://doi.org/10.5281/zenodo.22096604

## Phase II — Positive four-mode global control — COMPLETE

For

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),\qquad (\mu,c)\in\{1,3\}^2,
\]

the following are complete:

- global reset to \(1\);
- five-case smaller-target-source lemma;
- strong-induction generation \(1\leadsto N\);
- global strong connectivity;
- universal target simple-cycle embedding;
- global escape control.

```text
FOUR_MODE_ODD_SYSTEM_GLOBAL_CONTROL = PROVED / FROZEN
```

Archived papers:

- English: https://doi.org/10.5281/zenodo.22104057
- 中文: https://doi.org/10.5281/zenodo.22104101

## Phase III — Signed odd global control — COMPLETE

- sign-reflection conjugacy;
- negative odd global control;
- explicit \(1\leftrightarrow-1\) bridges;
- signed odd global strong connectivity;
- signed cycle embedding;
- escape to both signs of infinity.

```text
SIGNED_ODD_GLOBAL_CONTROL = PROVED / FROZEN
SIGN_MIRROR != TIME_REVERSAL
```

## Phase IV — W-NIGECT nonzero-integer microdynamics — COMPLETE

Expose the microdynamics:

- nonzero odd states: controlled affine transition \(n\mapsto\mu n+c\);
- nonzero even states: forced halving \(n\mapsto n/2\);
- zero: valid terminal target only, with no outgoing transition.

Complete results:

- micro/macro equivalence;
- exact even targeting;
- exact dyadic-position targeting;
- global strong connectivity on \(\mathbb Z\setminus\{0\}\);
- all-integer exact targetability from every nonzero source;
- universal nonzero-integer cycle embedding;
- escape to both signs of infinity.

```text
W_NIGECT = PROVED / FROZEN
NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN
```

Archived W-NIGECT papers:

- English: https://doi.org/10.5281/zenodo.22109060
- 中文: https://doi.org/10.5281/zenodo.22108987

## Phase V — Passive deterministic branch / universal outcome — CURRENT CORE OPEN PROGRAM

Fix the classical positive policy:

\[
(\mu,c)=(3,1).
\]

The forward route is unique. The principal remaining question is outcome:

\[
\forall n>0\text{ odd},\ \exists k:\ T^k(n)=1\ ?
\]

This is exactly the classical Collatz conjecture.

Priority research directions:

- identify which structural information from the controlled parent systems survives after the control alphabet is frozen;
- characterize the residue-imposed UP/FOLD sequence of the fixed branch;
- exclude nontrivial fixed-branch cycles;
- exclude unbounded fixed-branch positive-integer orbits;
- continue finite-alphabet / Source-Lock / residue-transport analysis where it directly constrains the passive branch.

## Independent technical program — NOT REQUIRED for completed control theorems

- PLDT;
- MPD18;
- pure-\(F\) periodicity;
- pure-\(F\) cycle classification;
- higher \(\nu_3=2\) residue-cylinder analysis.

## Publication / prior-art track

- Maintain each theorem layer as a separate archived paper.
- Continue prior-art review for signed affine controls and full nonzero-integer exact controllability.
- Do not claim control-alphabet minimality unless separately proved.

```text
GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
```
