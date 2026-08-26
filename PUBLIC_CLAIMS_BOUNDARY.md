# Public Claims Boundary

This repository documents mathematical research on Collatz-type discrete dynamics.

- A theorem is labeled **PROVED** only after a complete symbolic argument has been independently checked.
- Numerical search, residue census, or finite enumeration is **FINITE OBSERVATION** unless it is itself an exhaustive proof for the stated finite domain.
- The fixed-multiplier \(+1/+3\) system is not the standard fixed-\(+1\) Collatz map.
- The positive four-mode system is a controlled parent system, not the standard Collatz map.
- W-NIGECT extends the controlled parent system to signed nonzero-integer microdynamics; it still does **not** prove the fixed classical Collatz conjecture.
- Sign reflection is a conjugacy that preserves arrow orientation; it is not time reversal.
- Results labeled **BYPASSED / NOT REQUIRED** remain open as standalone mathematical statements unless separately proved.
- Novelty is not claimed without prior-art review.

## Formal W-NIGECT boundary

Active control domain:

\[
\mathcal D_{\mathrm{active}}=\mathbb Z\setminus\{0\}.
\]

Exact target domain:

\[
\mathcal T=\mathbb Z.
\]

Rules:

- nonzero odd state: controlled affine transition \(n\mapsto\mu n+c\), \(\mu\in\{1,3\}\), \(c\in\{-3,-1,1,3\}\);
- nonzero even state: forced transition \(n\mapsto n/2\);
- zero: valid terminal target only; no outgoing transition is defined;
- a finite path may terminate at any reached target vertex, including a nonzero even target;
- the signed odd-part macro-map is a compressed representation of the nonzero microtrajectory and is not defined at zero.

Therefore:

```text
CONTROL_DOMAIN = NONZERO_INTEGERS
TARGET_DOMAIN = ALL_INTEGERS

ZERO = VALID_TERMINAL_TARGET
ZERO = NOT_AN_ACTIVE_CONTROL_STATE
ZERO = OUTSIDE_SIGNED_ODDPART_MACRO_DOMAIN
NO_TRANSITION_IS_DEFINED_FROM_ZERO

NONZERO_INTEGER_GLOBAL_STRONG_CONNECTIVITY = PROVED / FROZEN
ALL_INTEGER_EXACT_TARGETABILITY_FROM_NONZERO_SOURCE = PROVED / FROZEN
FULL_INTEGER_STRONG_CONNECTIVITY = NOT_CLAIMED

SIGN_MIRROR != TIME_REVERSAL

GLOBAL_COLLATZ = OPEN
W-NIGECT != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
