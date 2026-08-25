# Public Claims Boundary

This repository documents mathematical research on Collatz-type discrete dynamics.

- A theorem is labeled **PROVED** only after a complete symbolic argument has been independently checked.
- Numerical search, residue census, or finite enumeration is **FINITE OBSERVATION** unless it is itself an exhaustive proof for the stated finite domain.
- The fixed-multiplier \(+1/+3\) system is not the standard fixed-\(+1\) Collatz map.
- The four-mode system \((\mu,c)\in\{1,3\}^2\) is a controlled parent system, not the standard Collatz map.
- Global controllability of the four-mode system does **not** prove convergence of the fixed mode \((3,1)\).
- A mixed or four-mode controlled cycle is not a counterexample to the classical Collatz conjecture.
- Forward-route uniqueness of the fixed mode is definitional; universal terminal outcome \(1\) is a separate open statement.
- Results labeled **BYPASSED / NOT REQUIRED** remain open as standalone mathematical statements unless separately proved.
- Novelty is not claimed without prior-art review.
- All dynamical theorem statements are restricted to positive integers and positive odd accelerated states.

```text
DOMAIN = POSITIVE_INTEGERS_ONLY
ODD_STATE_DOMAIN = N_ODD_POSITIVE
NEGATIVE_RATIONAL_REAL_PADIC_OBJECTS = OUTSIDE_THEOREM_DOMAIN

FOUR_MODE_ODD_SYSTEM_GLOBAL_CONTROL = PROVED / FROZEN
GLOBAL_COLLATZ = OPEN
FOUR_MODE_GLOBAL_CONTROL != STANDARD_COLLATZ_PROOF
PASSIVE_FORWARD_ROUTE_UNIQUENESS != UNIVERSAL_PASSIVE_OUTCOME
DUAL/MIXED_CONTROLLED_CYCLE != STANDARD_COLLATZ_COUNTEREXAMPLE
NOVELTY_NOT_CLAIMED_WITHOUT_PRIOR_ART_REVIEW
```
