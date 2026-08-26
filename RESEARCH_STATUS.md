# Research Status

“Frozen” means fixed for this public research index after symbolic proof and independent red-team checking; it is not a claim of peer-reviewed priority.

## PROVED / FROZEN — Layer I: fixed-multiplier local control

| Result | Status | Boundary |
|---|---|---|
| W-MPOCCT | PROVED / FROZEN | Fixed multiplier \(\mu=3\); local control-option completeness |
| Dyadic threshold | PROVED / FROZEN | Exact inequalities |
| +1/+3 valuation complementarity | PROVED / FROZEN | Every positive odd input |
| Positive-odd image partition by mod 3 | PROVED / FROZEN | Exact image statement |
| Local UP/FOLD polarity | PROVED / FROZEN | Positive odd \(n>3\) |
| RESET / ESCAPE in fixed-\(\mu=3\) mixed system | PROVED / FROZEN | Controlled policies |

**Archived Layer I paper:** https://doi.org/10.5281/zenodo.22096604

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

### Archived Layer II papers

- **English:** https://doi.org/10.5281/zenodo.22104057
- **中文：** https://doi.org/10.5281/zenodo.22104101

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

```text
W_NIGECT = PROVED / FROZEN
NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN
```

### Archived W-NIGECT papers

- **English:** *Global Exact Controllability of the Nonzero-Integer Microdynamics under Signed Affine Controls and Forced Halving*  
  https://doi.org/10.5281/zenodo.22109060
- **中文：**《带符号仿射控制与强制二分下非零整数微动力的全局精确可控性》  
  https://doi.org/10.5281/zenodo.22108987

## BYPASSED / NOT REQUIRED for Layer II and Layer IV proofs

These remain open as standalone mathematics unless separately proved:

- PLDT;
- MPD18;
- pure-\(F\) non-descending periodicity;
- pure-\(F\) cycle classification;
- higher residue-cylinder closure for \(\nu_3=2\).

## RETAINED OPEN — fixed passive Collatz branches

| Problem | Status |
|---|---|
| Classical fixed-\((3,1)\) Collatz conjecture | OPEN |
| Universal passive outcome \(=1\) | OPEN; exactly Collatz |
| Fixed +3 global reset | OPEN; Collatz-equivalent |
| Original fixed-multiplier \(\mu=3\), +1/+3 global control completeness | OPEN |

```text
GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
```
