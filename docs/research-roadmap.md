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

Archived papers:

- English: https://doi.org/10.5281/zenodo.22109060
- 中文: https://doi.org/10.5281/zenodo.22108987

## Phase V — Standard accelerated Collatz structural proof — PROJECT COMPLETE / EXTERNAL AUDIT PENDING

The passive standard map is

\[
U(n)=\operatorname{oddpart}(3n+1).
\]

The project proof architecture is built from the following bottom-up chain:

1. complete dyadic base map
   \[
   A(n)=\operatorname{oddpart}(n+1),
   \qquad
   n=2^aq-1;
   \]
2. exact standard inverse grammar
   \[
   U(p)=q\iff3p+1=2^bq;
   \]
3. LIVE / SOURCE interface exhaustion;
4. complete direct-root entrance family
   \[
   G_m=\frac{4^m-1}{3};
   \]
5. threefold folding and power-depth deformation
   \[
   U(P_a(q))=P_{a-1}(3q),
   \qquad
   U^a(P_a(q))=\operatorname{oddpart}(3^aq-1);
   \]
6. finite exact inverse words;
7. merge-suffix inheritance;
8. rooted-suffix closure under all power lifts;
9. rooted-suffix totality.

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
```

Archived papers:

- English: https://doi.org/10.5281/zenodo.22182820
- 中文: https://doi.org/10.5281/zenodo.22182736

See: [Layer V structural overview](dyadic-base-map-threefold-folding-global-completeness.md).

## Phase VI — Exact finite valuation geometry and root-anchored certificates — ACTIVE

This phase preserves research-history continuity by separating finite geometric refinement from the Layer V global-completeness manuscript.

Core exact ledger:

\[
2^{A_K}n_K=3^Kn_0+C_w.
\]

Two different walls are tracked:

\[
P_w=2^{A_K}-3^K
\]

and

\[
H_w(n_0)=C_w-P_wn_0,
\]

with

\[
2^{A_K}(n_K-n_0)=H_w(n_0).
\]

Active tasks:

- partial dyadic-tail geometry \((P^\partial,H^\partial)\);
- root-anchored exact certificate formalism;
- port-resolved finite inverse genealogy;
- exact \(2\)-adic branch-separation laws;
- compact MergeDAG organization;
- structural translation and classification of finite paradoxical/stopping-window catalogs.

## Phase VII — External proof audit and publication hardening — ACTIVE

Priority tasks:

- independent line-by-line verification of the rooted-suffix closure theorem;
- exact counterexample qualification: objections must identify a failing formula, hypothesis, implication, or legal integer witness;
- prior-art audit of elementary/classical components versus the project's interface architecture;
- reproducibility packages and machine-checkable finite certificates;
- journal-format preparation after independent mathematical review.

## Separate technical programs — NOT REQUIRED for the frozen Layer V implication chain

- PLDT;
- MPD18;
- legacy minimum-port periodicity;
- older residue-cylinder subprograms;
- brute-force expansion of numerical verification bounds when no new structure is produced.

## Publication discipline

- maintain each theorem layer as a separate archived paper;
- distinguish exact theorem, definition, finite computation, conjecture, and external review status;
- do not claim novelty for classical affine or inverse formulas without prior-art review;
- preserve the chronological discovery chain so later papers extend rather than overwrite earlier layers.

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
PROJECT_PROOF_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE
```
