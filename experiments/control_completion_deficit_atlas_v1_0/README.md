# Control-Completion Deficit Atlas v1.0

This incremental experiment studies what local control options are removed when
the four-mode positive-odd system

\[
V_{\mu,c}(n)=\operatorname{oddpart}(\mu n+c),
\qquad (\mu,c)\in\{1,3\}^2
\]

is frozen to the passive accelerated Collatz branch \((\mu,c)=(3,1)\).

It does not test or claim global Collatz convergence. Logarithmic deficits are
counterfactual local diagnostics, not distances between two realized orbits.

## Reproduction

From this directory, using Python 3.11 or newer:

```text
python -m unittest discover -s tests -v
python run_atlas.py --config config.json --output outputs
python verify_outputs.py --root .
```

`state_sample.parquet` requires `pyarrow`; all exact maps and CSV outputs use
the Python standard library and arbitrary-precision integers. Large integer
fields in the Parquet sample are stored as exact decimal strings.

The 500,000-row Tier B summary is emitted as two ordered 250,000-row CSV
parts so every GitHub object remains below 100 MB. Extracting or concatenating
data rows in part order reconstructs the full table; each part includes the
same header.

## Scope

```text
DOMAIN = POSITIVE_INTEGERS_ONLY
ODD_STATE_DOMAIN = N_ODD_POSITIVE
FOUR_MODE_GLOBAL_CONTROL = PROVED / INPUT THEOREM
PASSIVE_COLLATZ_BRANCH = FIXED (3,1)
GLOBAL_COLLATZ = OPEN
NUMERICAL_EVIDENCE != PROOF
```
