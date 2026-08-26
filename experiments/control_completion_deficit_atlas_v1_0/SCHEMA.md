# Data Scope and Schema Notes

## Full-domain tables

- `outputs/orbit_summary_1e6_part01_of_02.csv` and
  `outputs/orbit_summary_1e6_part02_of_02.csv`: 250,000 rows each, jointly
  covering every positive odd start in `1 <= n <= 1,000,000`. Both carry the
  identical complete header. The split keeps every GitHub object below its
  100 MB hard limit without removing fields.
- `outputs/orbit_summary_tier_c.csv`: one row for each of 50,000 distinct odd
  starts sampled without replacement from `[1, 10^12]` with public seed
  `20260826`.
- `outputs/residue_signature_atlas.csv`: all 252 odd residue rows across moduli
  8, 16, 32, 64, 128, and 256.

## Complete named trajectories

`outputs/named_orbits.csv` contains every nonterminal accelerated odd state and
an explicit terminal row for starts 27, 97, 871, and 6171. Integer map outputs,
valuations, residues, directions, and exact ratio numerators/denominators are
stored directly. Logarithmic columns are diagnostics.

## Deterministic analysis cohort

Event-level tables use a fixed, reproducible cohort to avoid duplicating common
Collatz tails into multi-gigabyte CSV files:

- all four named starts;
- 4,096 Tier B starts selected by the public seed;
- 4,096 Tier C starts selected by the public seed.

This gives 8,196 labelled orbit records. The selection algorithm and seed are
in `run_atlas.py` and `config.json`.

- `compensation_events.csv`: every `a31 >= 3` event in the cohort.
- `debt_peak_events.csv`: every new cumulative reset-debt peak in the cohort.
- `passive_runs.csv`: every maximal U1 and `{1,2}`-alphabet run in the cohort.
- `state_sample.parquet`: deterministic 100,000-row priority sample from the
  cohort. Arbitrary-precision integer columns use exact decimal strings.

## Symbolic and control tables

- `sturmian_summary.json`: one-million-symbol mechanical-word check, candidate
  formula comparison, complexity, run, and macro statistics.
- `sturmian_factors.csv`: present/forbidden factors through length 16 and all
  present factors for lengths 17 through 64.
- `natural_vs_sturmian.csv`: four named orbits and the top 100 Tier B
  critical-like records.
- `hypothesis_tests.csv`: H1–H5 statistics and the required shuffle, segment,
  iid, and random-balanced-word negative controls.
- `record_cases.csv`: top 100 Tier B records under five ranking metrics.

## Status vocabulary

`UNRESOLVED_WITHIN_CAP` is right-censored, never divergent. All numerical
results are finite observations or exact certificates for their stated finite
domains.

```text
GLOBAL_COLLATZ = OPEN
NUMERICAL_EVIDENCE != PROOF
```
