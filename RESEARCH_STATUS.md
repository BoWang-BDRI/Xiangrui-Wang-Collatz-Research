# Research Status

“Frozen” means fixed for this public research index after symbolic proof and independent red-team checking; it is not by itself a claim of peer-reviewed priority or community acceptance.

## PROVED / FROZEN — Layer I: fixed-multiplier local control

| Result | Status | Boundary |
|---|---|---|
| W-MPOCCT | PROVED / FROZEN | Fixed multiplier \(\mu=3\); local control-option completeness |
| Dyadic threshold | PROVED / FROZEN | Exact inequalities |
| +1/+3 valuation complementarity | PROVED / FROZEN | Every positive odd input |
| Positive-odd image partition by mod 3 | PROVED / FROZEN | Exact image statement |
| Local UP/FOLD polarity | PROVED / FROZEN | Positive odd \(n>3\) |
| RESET / ESCAPE in fixed-\(\mu=3\) mixed system | PROVED / FROZEN | Controlled policies |

Archived Layer I paper: https://doi.org/10.5281/zenodo.22096604

## PROVED / FROZEN — Layer II: positive four-mode global control

For

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),\qquad (\mu,c)\in\{1,3\}^2,
\]

the following are frozen:

| Result | Status |
|---|---|
| Exact closure on positive odd states | PROVED / FROZEN |
| Global reset to \(1\) via \((1,1)\) | PROVED / FROZEN |
| Five-case target-source lemma | PROVED / FROZEN |
| Uniform source bound \(p<8N/9\) | PROVED / FROZEN |
| Global generation \(1\leadsto N\) | PROVED / FROZEN |
| Global strong connectivity | PROVED / FROZEN |
| Universal target simple-cycle embedding | PROVED / FROZEN |
| Global escape control | PROVED / FROZEN |

Archived Layer II papers:

- English: https://doi.org/10.5281/zenodo.22104057
- 中文: https://doi.org/10.5281/zenodo.22104101

## PROVED / FROZEN — Layer III: signed odd global control

On nonzero odd states, allow

\[
\mu\in\{1,3\},\qquad c\in\{-3,-1,1,3\}.
\]

Frozen results:

| Result | Status |
|---|---|
| Full sign conjugacy | PROVED / FROZEN |
| Negative odd global control | PROVED / FROZEN |
| Signed odd global strong connectivity | PROVED / FROZEN |
| Signed odd universal cycle embedding | PROVED / FROZEN |
| Escape to both signs of infinity | PROVED / FROZEN |

```text
SIGN_MIRROR != TIME_REVERSAL
```

## PROVED / FROZEN — Layer IV: W-NIGECT full nonzero-integer microdynamics

Active control domain:

\[
\mathcal D_{\mathrm{active}}=\mathbb Z\setminus\{0\}.
\]

Target domain:

\[
\mathcal T=\mathbb Z.
\]

Rules:

- nonzero odd states: controlled affine step \(n\mapsto\mu n+c\), with \(\mu\in\{1,3\}\), \(c\in\{-3,-1,1,3\}\);
- nonzero even states: forced halving \(n\mapsto n/2\);
- zero: valid terminal target, not an active state, and no transition is defined from zero.

| Result | Status |
|---|---|
| Micro/macro equivalence | PROVED / FROZEN |
| Complete six zero-terminal edge list | PROVED / FROZEN |
| Exact even targeting | PROVED / FROZEN |
| Exact dyadic-position targeting | PROVED / FROZEN |
| Nonzero-integer global strong connectivity | PROVED / FROZEN |
| Nonzero-integer global exact control | PROVED / FROZEN |
| Universal nonzero-integer cycle embedding | PROVED / FROZEN |
| Escape to \(+\infty\) and \(-\infty\) | PROVED / FROZEN |
| All-integer exact targetability from nonzero source | PROVED / FROZEN |

Archived W-NIGECT papers:

- English: https://doi.org/10.5281/zenodo.22109060
- 中文: https://doi.org/10.5281/zenodo.22108987

## PROJECT-PROVED / EXTERNAL REVIEW PENDING — Layer V: standard accelerated Collatz odd system

Define

\[
A(n)=\operatorname{oddpart}(n+1),
\qquad
U(n)=\operatorname{oddpart}(3n+1).
\]

The current Layer V project proof architecture freezes the following symbolic components:

| Result | Project status |
|---|---|
| Complete dyadic base tree \(n=2^aq-1\) | PROVED / FROZEN |
| Exact accelerated edge grammar \(U(p)=q\iff3p+1=2^bq\) | PROVED / FROZEN |
| LIVE / SOURCE odd-interface exhaustion | PROVED / FROZEN |
| Complete direct-root family \(G_m=(4^m-1)/3\) | PROVED / FROZEN |
| \(\nu_3(G_m)=\nu_3(m)\) and ROOT/LIVE/SOURCE entrance trichotomy | PROVED / FROZEN |
| Threefold folding / power-depth deformation | PROVED / FROZEN |
| Finite exact inverse-word grammar | PROVED / FROZEN |
| Merge suffix inheritance | PROVED / FROZEN |
| Rooted generative object formulation: integer state + inherited finite standard-\(U\) suffix genealogy | PROVED / FROZEN — project formulation |
| Rooted suffix closure under power lifts | PROVED / FROZEN — project theorem |
| Rooted generative totality | PROVED / FROZEN — project theorem |
| Standard positive-integer Collatz conclusion | PROVED / FROZEN — project claim; external review pending |

The decisive coordinates include

\[
P_a(q)=2^aq-1,
\]

\[
U(P_a(q))=P_{a-1}(3q)\quad(a\ge2),
\]

and

\[
U^a(P_a(q))=\operatorname{oddpart}(3^aq-1).
\]

All direct-to-root odd states are

\[
G_m=\frac{4^m-1}{3}.
\]

The current proof object is not an isolated integer with a free residual variable. Each generated state is bound to its finite rooted genealogy; affine corrections and residuals are treated as derived ledgers of a finite chain rather than independent dynamical degrees of freedom.

### Archived Layer V papers

- **Latest English complete-analysis paper:** *Dyadic Base Map, Threefold Folding, Rooted Generative Coverage, and Global Normalization in the Accelerated Collatz Odd System (A Complete Analysis of the Collatz Conjecture)*  
  https://doi.org/10.5281/zenodo.22246883
- **Earlier English architecture record:** *Dyadic Base Map, Threefold Folding, Entrance Transfer, and Global Completeness in the Accelerated Collatz Odd System*  
  https://doi.org/10.5281/zenodo.22182820
- **中文：**《加速考拉兹奇数系统的二幂底图、三倍折叠、入口迁移与全局完备性》  
  https://doi.org/10.5281/zenodo.22182736

### Status firewall

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
PROJECT_PROOF_ARCHIVED_ON_ZENODO = YES
LATEST_PROJECT_PROOF_DOI = 10.5281/zenodo.22246883
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN
```

The repository therefore records two different statements and does not conflate them:

1. the project contains a frozen symbolic proof claiming global completeness;
2. the classical Collatz conjecture remains open in the wider mathematical community until the proof receives independent external validation and acceptance.

## FINITE EXACT COMPANION — valuation geometry and root-anchored certificates

This series is separated from the Layer V global-completeness paper. Its archived English paper is:

**Exact Valuation Geometry and Root-Anchored Certificates for the Accelerated Collatz Map I: Affine Height, Dyadic Normalization Ports, and Finite Inverse Words**  
https://doi.org/10.5281/zenodo.22197750

Exact finite structures include:

| Result / object | Status |
|---|---|
| Affine ledger \(2^{A_K}n_K=3^Kn_0+C_w\) | PROVED |
| Multiplicative coefficient gap \(P_w=2^{A_K}-3^K\) | PROVED |
| Actual height margin \(H_w=C_w-P_wn_0\) | PROVED |
| Exact identity \(2^{A_K}(n_K-n_0)=H_w\) | PROVED |
| Partial-tail \(P^\partial,H^\partial\) criterion | PROVED |
| Valuation-word / binary-word encoding | PROVED |
| First-discrepancy \(2\)-adic separation | PROVED |
| Root-anchored finite exact certificate | DEFINED / structurally valid |

## Research chronology relevant to the current Layer V proof

1. Global exact controllability in the enlarged signed nonzero-integer system — `10.5281/zenodo.22109060`.
2. Dyadic base / threefold-folding / entrance-transfer architecture for the fixed standard map — `10.5281/zenodo.22182820`.
3. Finite exact valuation geometry and root-anchored certificates — `10.5281/zenodo.22197750`.
4. Rooted generative coverage and global normalization complete analysis — `10.5281/zenodo.22246883`.

## BYPASSED / separate technical programs

These are no longer premises of the Layer V project proof and remain separate research objects unless independently completed:

- PLDT;
- MPD18;
- earlier minimum-port maps;
- residue-cylinder subprograms;
- legacy stopping-time and parity-window scans.

## Repository-wide guardrails

```text
PROJECT_GLOBAL_COLLATZ = PROVED / FROZEN
LATEST_PROJECT_PROOF_DOI = 10.5281/zenodo.22246883
EXTERNAL_INDEPENDENT_REVIEW = PENDING
COMMUNITY_STATUS_OF_COLLATZ = OPEN

W_NIGECT = PROVED / FROZEN
W-NIGECT != STANDARD_COLLATZ_PROOF

NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
PROJECT_PROOF_STATUS != PEER_REVIEWED_COMMUNITY_ACCEPTANCE
```
