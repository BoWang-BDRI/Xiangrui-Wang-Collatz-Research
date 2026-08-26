# Exact Reproduction Commands

Commands were run from the repository root on Windows with Python 3.12.

## Isolated dependency environment

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install pyarrow==25.0.1
```

The virtual environment is excluded by `.gitignore` and is not committed.

## Tests

```powershell
Set-Location .\experiments\control_completion_deficit_atlas_v1_0
..\..\.venv\Scripts\python.exe -m py_compile run_atlas.py verify_outputs.py src\control_deficit_core.py tests\test_exact.py
..\..\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

## Full run

```powershell
..\..\.venv\Scripts\python.exe run_atlas.py --config config.json --output outputs
```

Recorded full-run wall time: approximately 241 seconds. The run prints progress
after each 100,000 Tier B starts.

## Manifest and independent replay

After `REPORT.md` and all output files are final:

```powershell
..\..\.venv\Scripts\python.exe verify_outputs.py --root . --write-manifest
..\..\.venv\Scripts\python.exe verify_outputs.py --root .
```

The second command rehashes every manifest member, streams all 500,000 Tier B
and 50,000 Tier C summary rows, replays every named and Parquet state, verifies
the residue atlas, and checks the Sturmian and scope boundaries.
