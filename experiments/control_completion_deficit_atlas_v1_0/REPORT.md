# Control-Completion Deficit Atlas v1.0 — Report

## 1. Scope and claims boundary

The input theorem is the frozen four-mode positive-odd control system

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),
\qquad (\mu,c)\in\{1,3\}^2.
\]

This experiment freezes the realized route to the passive branch
\(T(n)=V_{3,1}(n)\). The other three modes are local counterfactual options.
The reset and best-hidden deficits are sums of local comparisons, not distances
between two realized trajectories.

```text
DOMAIN = POSITIVE_INTEGERS_ONLY
ODD_STATE_DOMAIN = N_ODD_POSITIVE
PASSIVE_FORWARD_ROUTE_UNIQUENESS = DEFINITIONAL
GLOBAL_COLLATZ = OPEN
NUMERICAL_EVIDENCE != PROOF
```

## 2. Exact sanity check

All 500,000 positive odd inputs in `1 <= n <= 1,000,000` passed the nine
required exact checks. The states 1 and 3 were handled separately from the
`n > 3` inequalities. There were zero failures in:

1. positivity and oddness of A/B/C/D;
2. C/D valuation complementarity;
3. strict A and B descent for `n > 3`;
4. exactly one UP and three FOLD modes;
5. the C non-3 sheet and D multiple-of-3 sheet partition;
6. mod-4 direction equivalence;
7. all four specified mod-8 valuation rules.

The passive height cocycle was also replayed:

\[
\sum_{k<K}g_k=\log_2(n_K/n_0),
\qquad g_k=-\epsilon_k+\eta_k.
\]

The maximum absolute floating evaluation residual across the two full scan
tiers was `7.106e-15`; the state transitions themselves were exact integers.

## 3. Natural-integer tiers

| Tier | Starts | Result within cap | Largest odd-step count | Largest odd value |
|---|---:|---|---:|---:|
| B: all odd starts through 1,000,000 | 500,000 | 500,000 reached 1 | 195 at 837799 | 18,997,161,173 at 704511 |
| C: fixed-seed odd sample through 10^12 | 50,000 | 50,000 reached 1 | 306 at 493510750181 | 5,050,151,167,886,225 at 369529341167 |

These are finite observations. Zero cap survivors is not a global convergence
claim.

### Complete named-orbit diagnostics

| Start | Odd steps | Maximum odd state | U1/F2/F3/F4P | Max U1 burst | Final reset deficit | Max reset deficit | Final best-hidden deficit |
|---:|---:|---:|---|---:|---:|---:|---:|
| 27 | 41 | 3,077 | 24/10/3/4 | 5 | 84.4801 | 88.4980 | 117.7772 |
| 97 | 43 | 3,077 | 24/11/4/4 | 5 | 82.6789 | 86.6968 | 122.9528 |
| 871 | 65 | 63,665 | 38/14/6/7 | 5 | 138.6189 | 142.6369 | 195.9845 |
| 6171 | 96 | 325,133 | 54/25/10/7 | 5 | 188.6707 | 192.6886 | 278.9305 |

Every state and exact ratio is in `outputs/named_orbits.csv`.

## 4. Reset debt and passive compensation

The strongest H1 result is a counterexample to the proposed simple direction.
In the actual arithmetic sequence, the highest recent reset-debt decile was
**less**, not more, likely to be followed by `a31 >= 3`:

| Window | P(deep fold), lowest Q decile | P(deep fold), highest Q decile | High minus low |
|---:|---:|---:|---:|
| 4 | 0.3045 | 0.1802 | -0.1243 |
| 8 | 0.3467 | 0.2384 | -0.1082 |
| 16 | 0.3120 | 0.2784 | -0.0337 |
| 32 | 0.2896 | 0.2558 | -0.0338 |
| 64 | 0.2636 | 0.2615 | -0.0022 |

The effect is short-range and fades by W=64. The complete-orbit-segment and
iid controls are nearly flat at W=4 and W=8; within-orbit shuffling retains a
smaller difference, showing that part of the signal is marginal/orbit
composition and part is arithmetic ordering. This is association, not
causation.

Among 374,124 debt-peak events in the deterministic analysis cohort, 53,410
(14.28%) returned below the pre-peak level before termination; 320,714 were
right-censored. For events with a later deep fold, the wait to `a31 >= 3` had
median 3, 90th percentile 9, and maximum 37. The wait to `a31 >= 4` had median
6, 90th percentile 20, and maximum 71. Repaid peaks had median repayment time
2, 90th percentile 5, and maximum 25 steps.

An exact finite counterexample to prompt compensation occurs in sampled orbit
`start=118074066123`: a peak at index 19 and state 15,601,579 waits 37 odd steps
for the next `a31 >= 3`, reaches 12,479,158,997 before termination, and never
returns below its pre-peak debt level. This is not a Collatz counterexample.

## 5. Best-hidden and direction deficits

In the deterministic 100,000-state sample:

- reset deficit was positive in 74.51% of rows;
- best-hidden deficit was positive in 93.29% of rows;
- their Pearson correlation was 0.797;
- the best hidden mode was A in 50.132% and B in 49.868%; D was never the
  minimum in this sample;
- best-hidden and reset deficit were identical on every sampled U1 event.

Depth resolves the reset-deficit sign more sharply: U1 and F2 samples were all
positive, while F3 and F4P samples were all negative. Best-hidden debt is much
more often positive and therefore less discriminating; it is largely a lower
baseline rather than a new compensation signal.

The direction deficit is exact but local. A passive UP row has three deleted
down moves; a passive FOLD row has two deleted down moves and one deleted up
move. This is a useful control-loss signature, not a forward prediction.

## 6. López–Stoll critical Sturmian experiment

The upper mechanical word and the candidate odd-return formula agreed at all
first 1,000,000 indices with no intercept or indexing correction:

\[
a_i=1+\lfloor(i+1)\log_2(3/2)\rfloor
-\lfloor i\log_2(3/2)\rfloor.
\]

The finite prefix had frequencies `a=1: 0.415038` and `a=2: 0.584962`, no
consecutive `a=1`, maximum F2 run 2, and the complete macro partition
`UF=245114`, `UFF=169924`. Factor complexity satisfied `p(L)=L+1` for every
`1 <= L <= 64`.

The skeleton removes both `n == 5 (mod 8)` deep-fold ports and `n == 7 (mod
8)` repeated-UP ports. This is a symbolic word statement only; no positive
natural source for the infinite word is asserted.

## 7. Natural trajectories versus the critical language

Long `{1,2}` alphabet runs are not generally critical Sturmian factors:

- Tier B maximum `{1,2}` run: 51 at start 917161;
- Tier B maximum genuine factor match: 14 at start 683943, beginning at state
  1,025,915 with word `12122121212212`;
- Tier C maximum genuine factor match: 15 at start 257050265803, beginning at
  state 41,220,974,459 with word `121221212212121`.

In the deterministic natural-window sample, only 0.8437% of `{1,2}` windows of
length 8 belonged to the critical language, and none of the 4,573 sampled
length-16 alphabet windows did. By contrast, the same-frequency random balanced
word contained all 256 length-8 factors and 65,281 of 65,536 length-16 factors.

Across all 500,000 Tier B starts, the first critical-prefix break was a deep
fold for 290,658 starts and a critical forbidden grammar event for 209,341;
the remaining case is terminal start 1. This is strong finite evidence that
“bounded valuation alphabet” and “critical Sturmian language” are different
constraints. It is not a uniform bound or eventual-periodicity theorem.

## 8. Deep-fold dyadic cylinders

Repayment size is strongly concentrated by the exact dyadic valuation
cylinders, but the leading pattern is valuation-driven rather than a new
independent mechanism. Examples from the full Tier B event aggregate are:

- `n == 5 (mod 16)`: mean `-delta_R = 2.1432`;
- `n == 13 (mod 16)`: mean `-delta_R = 0.4242`;
- `n == 85 (mod 256)`: mean `-delta_R = 6.4446`, corresponding to the
  `a31 >= 8` cylinder;
- `n == 213 (mod 256)`: mean `-delta_R = 4.4152`.

The atlas writes lower bounds such as `a31 >= r` whenever the modulus does not
determine an exact valuation. No higher valuation is guessed.

## 9. Sheet loss and passive residue grammar

Every passive C output remains on the non-multiple-of-3 sheet; the deleted D
branch is the direct multiple-of-3 sheet switch. The full Tier B transition
counts contained 22,996,390 passive transitions. At moduli 3, 9, 27, and 81,
the target sets occupied respectively 2, 6, 18, and 54 residues: exactly the
non-multiples of 3. The observed finer movement grammar therefore does not
compensate by recovering the missing sheet.

## 10. Strongest pattern, strongest counterexample, and best observable

- **Strongest compensation pattern:** short-window arithmetic sequencing is
  real relative to segment and iid controls, but its sign is inverse to H1.
- **Strongest counterexample:** high reset debt does not force prompt deep
  folding; the 37-step wait above is an exact finite witness.
- **Longest critical-like run:** length 15 in Tier C; the much longer alphabet
  run of 51 is not a critical-language factor.
- **Most valuable new observable:** the exact critical-language residual
  `(longest compatible factor, first break type)`. It separates finite-alphabet
  pressure from actual Sturmian structure without a floating threshold.

## 11. PROVED / EXPERIMENTAL / OPEN separation

### PROVED / INPUT THEOREM

- The four-mode global control result is accepted as the frozen input theorem.
- Passive branch uniqueness after fixing `(3,1)` is definitional.
- Map values, valuations, image sheets, and residue-atlas entries are exact.
- Individual stored trajectories and finite event certificates replay exactly.

### EXPERIMENTAL / FINITE

- Tier B and Tier C stopping, maxima, debt, correlation, and run statistics.
- H1–H5 comparisons and every negative control.
- The one-million-symbol Sturmian prefix comparison.
- Any usefulness ranking below.

### OPEN

- Classical Collatz convergence.
- Any uniform compensation bound.
- Realization of the infinite critical skeleton by a positive natural source.
- M-C17* closure, eventual periodicity, and global sheet compensation.

## 12. Final verdict

```text
FOUR_MODE_GLOBAL_CONTROL = PROVED / INPUT THEOREM

PASSIVE_COLLATZ_BRANCH = FIXED (3,1)

GLOBAL_COLLATZ = OPEN


CONTROL_DEFICIT_OBSERVABLES:

RESET_DEFICIT =
USEFUL

BEST_HIDDEN_DEFICIT =
WEAK

DIRECTION_DEFICIT =
USEFUL

SHEET_DEFICIT =
USEFUL

CRITICAL_RESIDUAL =
USEFUL


M-C17* RELEVANCE =
WEAKER


NEXT_THEOREM_CANDIDATE =
NONE
```

The RESET verdict means useful as a falsification/sequence diagnostic, not as
a confirmed compensation potential. No correlation in this atlas is promoted
to a theorem.
