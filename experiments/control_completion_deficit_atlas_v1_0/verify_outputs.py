#!/usr/bin/env python3
"""Independent replay and release verifier for the deficit atlas increment."""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))

from control_deficit_core import residue_signature_row, state_features  # noqa: E402


REQUIRED_OUTPUTS = {
    "named_orbits.csv",
    "orbit_summary_1e6_part01_of_02.csv",
    "orbit_summary_1e6_part02_of_02.csv",
    "orbit_summary_tier_c.csv",
    "state_sample.parquet",
    "compensation_events.csv",
    "debt_peak_events.csv",
    "passive_runs.csv",
    "sturmian_summary.json",
    "sturmian_factors.csv",
    "natural_vs_sturmian.csv",
    "residue_signature_atlas.csv",
    "hypothesis_tests.csv",
    "record_cases.csv",
    "sanity_checks.json",
    "run_summary.json",
}


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(8 * 1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def manifest_files(root: Path) -> list[Path]:
    result: list[Path] = []
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        relative = path.relative_to(root)
        if path.name == "MANIFEST.sha256" or "__pycache__" in relative.parts:
            continue
        result.append(path)
    return sorted(result, key=lambda path: path.relative_to(root).as_posix())


def write_manifest(root: Path) -> None:
    lines = [f"{sha256(path)}  {path.relative_to(root).as_posix()}" for path in manifest_files(root)]
    (root / "MANIFEST.sha256").write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")


def verify_manifest(root: Path) -> int:
    manifest = root / "MANIFEST.sha256"
    if not manifest.exists():
        raise AssertionError("MANIFEST.sha256 missing")
    recorded: dict[str, str] = {}
    for line in manifest.read_text(encoding="utf-8").splitlines():
        digest, relative = line.split("  ", 1)
        recorded[relative] = digest
    current = {path.relative_to(root).as_posix(): sha256(path) for path in manifest_files(root)}
    if recorded != current:
        missing = sorted(set(current) - set(recorded))
        extra = sorted(set(recorded) - set(current))
        mismatched = sorted(key for key in set(current) & set(recorded) if current[key] != recorded[key])
        raise AssertionError(f"manifest mismatch missing={missing} extra={extra} hashes={mismatched}")
    return len(current)


def count_and_validate_tier_b(paths: list[Path]) -> tuple[int, dict[str, int]]:
    count = 0
    statuses: dict[str, int] = {}
    previous = -1
    per_part: list[int] = []
    for path in paths:
        part_count = 0
        with path.open(encoding="utf-8", newline="") as handle:
            for row in csv.DictReader(handle):
                start = int(row["start_n"])
                expected = 2 * count + 1
                if start != expected:
                    raise AssertionError(f"Tier B start sequence {start} != {expected}")
                if start <= previous:
                    raise AssertionError("Tier B not strictly increasing")
                previous = start
                statuses[row["status"]] = statuses.get(row["status"], 0) + 1
                if row["status"] == "REACHED_1" and int(row["terminal_or_cap_state"]) != 1:
                    raise AssertionError(f"Tier B bad terminal at {start}")
                if abs(float(row["height_cocycle_error"])) > 1e-10:
                    raise AssertionError(f"Tier B cocycle error at {start}")
                count += 1
                part_count += 1
        per_part.append(part_count)
    if per_part != [250_000, 250_000]:
        raise AssertionError(f"Tier B part rows {per_part}")
    if count != 500_000:
        raise AssertionError(f"Tier B rows {count}")
    return count, statuses


def validate_tier_c(path: Path) -> tuple[int, dict[str, int]]:
    count = 0
    starts: set[int] = set()
    statuses: dict[str, int] = {}
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            start = int(row["start_n"])
            if not (1 <= start <= 10**12 and start % 2 == 1):
                raise AssertionError(f"Tier C start out of domain {start}")
            if start in starts:
                raise AssertionError(f"Tier C duplicate {start}")
            starts.add(start)
            statuses[row["status"]] = statuses.get(row["status"], 0) + 1
            if row["status"] not in {"REACHED_1", "UNRESOLVED_WITHIN_CAP", "REPEATED_STATE"}:
                raise AssertionError(f"Tier C invalid status {row['status']}")
            if abs(float(row["height_cocycle_error"])) > 1e-10:
                raise AssertionError(f"Tier C cocycle error at {start}")
            count += 1
    if count != 50_000:
        raise AssertionError(f"Tier C rows {count}")
    return count, statuses


def validate_named(path: Path) -> int:
    expected_index: dict[str, int] = {}
    previous_state: dict[str, int] = {}
    terminal_seen: set[str] = set()
    rows = 0
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            orbit = row["orbit_id"]
            index = int(row["odd_step_index"])
            if index != expected_index.get(orbit, 0):
                raise AssertionError(f"named index discontinuity {orbit}:{index}")
            expected_index[orbit] = index + 1
            n = int(row["n"])
            feature = state_features(n)
            observed = tuple(int(row[key]) for key in ("A", "B", "C", "D", "a11", "a13", "a31", "a33"))
            exact = (feature.A, feature.B, feature.C, feature.D, feature.a11, feature.a13, feature.a31, feature.a33)
            if observed != exact:
                raise AssertionError(f"named exact replay mismatch {orbit}:{index}")
            if orbit in previous_state and n != previous_state[orbit]:
                raise AssertionError(f"named transition mismatch {orbit}:{index}")
            if row["is_terminal"] == "1":
                if n != 1:
                    raise AssertionError(f"named non-one terminal {orbit}")
                terminal_seen.add(orbit)
            else:
                previous_state[orbit] = feature.C
            rows += 1
    if terminal_seen != {"NAMED_27", "NAMED_97", "NAMED_871", "NAMED_6171"}:
        raise AssertionError(f"named terminal set {terminal_seen}")
    return rows


def validate_parquet(path: Path) -> tuple[int, int]:
    import pyarrow.parquet as pq

    table = pq.read_table(path)
    if table.num_rows != 100_000:
        raise AssertionError(f"Parquet rows {table.num_rows}")
    required = {
        "n_exact_decimal", "A_exact_decimal", "B_exact_decimal", "C_exact_decimal",
        "D_exact_decimal", "a11", "a13", "a31", "a33",
    }
    if not required <= set(table.column_names):
        raise AssertionError("Parquet required schema missing")
    values = table.select(sorted(required)).to_pylist()
    for index, row in enumerate(values):
        n = int(row["n_exact_decimal"])
        feature = state_features(n)
        exact = (feature.A, feature.B, feature.C, feature.D, feature.a11, feature.a13, feature.a31, feature.a33)
        observed = (
            int(row["A_exact_decimal"]), int(row["B_exact_decimal"]),
            int(row["C_exact_decimal"]), int(row["D_exact_decimal"]),
            row["a11"], row["a13"], row["a31"], row["a33"],
        )
        if observed != exact:
            raise AssertionError(f"Parquet exact replay mismatch row {index}")
    return table.num_rows, table.num_columns


def validate_sturmian(path: Path) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    if data["odd_return_symbol_count"] != 1_000_000:
        raise AssertionError("Sturmian symbol count")
    if data["candidate_formula_mismatches"] != 0:
        raise AssertionError("Sturmian formula mismatch")
    if not data["factor_complexity_L_plus_1"]:
        raise AssertionError("Sturmian complexity flag")
    if {int(key): value for key, value in data["factor_complexity"].items()} != {
        length: length + 1 for length in range(1, 65)
    }:
        raise AssertionError("Sturmian p(L) mismatch")
    if data["positive_natural_source_claimed"]:
        raise AssertionError("forbidden positive-source claim")


def validate_atlas(path: Path) -> int:
    count = 0
    with path.open(encoding="utf-8", newline="") as handle:
        for row in csv.DictReader(handle):
            bits = int(row["bits"])
            residue = int(row["odd_residue"])
            exact = residue_signature_row(bits, residue)
            for key, value in exact.items():
                if str(row[key]) != str(value):
                    raise AssertionError(f"atlas mismatch mod={1<<bits} r={residue} key={key}")
            count += 1
    if count != 252:
        raise AssertionError(f"atlas rows {count}")
    return count


def validate_text_files(root: Path) -> int:
    count = 0
    user_path_signature = b"C:" + b"\\Users\\"
    drive_path_signature = b"D:" + b"\\"
    for path in manifest_files(root):
        if path.suffix.lower() in {".parquet", ".pyc"}:
            continue
        raw = path.read_bytes()
        if raw.startswith(b"\xef\xbb\xbf"):
            raise AssertionError(f"UTF-8 BOM {path}")
        if b"\r" in raw:
            raise AssertionError(f"non-LF line ending {path}")
        if user_path_signature in raw or drive_path_signature in raw:
            raise AssertionError(f"absolute path leak {path}")
        count += 1
    return count


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=HERE)
    parser.add_argument("--write-manifest", action="store_true")
    args = parser.parse_args()
    root = args.root.resolve()
    outputs = root / "outputs"
    missing = sorted(name for name in REQUIRED_OUTPUTS if not (outputs / name).exists())
    if missing:
        raise AssertionError(f"missing outputs {missing}")
    for name in ("README.md", "REPORT.md", "RUN_COMMANDS.md", "config.json", "run_atlas.py"):
        if not (root / name).exists():
            raise AssertionError(f"missing {name}")
    if args.write_manifest:
        write_manifest(root)

    manifest_count = verify_manifest(root)
    tier_b_rows, tier_b_status = count_and_validate_tier_b(
        [
            outputs / "orbit_summary_1e6_part01_of_02.csv",
            outputs / "orbit_summary_1e6_part02_of_02.csv",
        ]
    )
    tier_c_rows, tier_c_status = validate_tier_c(outputs / "orbit_summary_tier_c.csv")
    named_rows = validate_named(outputs / "named_orbits.csv")
    parquet_rows, parquet_columns = validate_parquet(outputs / "state_sample.parquet")
    validate_sturmian(outputs / "sturmian_summary.json")
    atlas_rows = validate_atlas(outputs / "residue_signature_atlas.csv")
    sanity = json.loads((outputs / "sanity_checks.json").read_text(encoding="utf-8"))
    if sanity["failures"] != 0:
        raise AssertionError("sanity failures nonzero")
    run = json.loads((outputs / "run_summary.json").read_text(encoding="utf-8"))
    if run["status"] != "FINITE_EXPERIMENT_COMPLETE" or run["global_collatz"] != "OPEN":
        raise AssertionError("run status boundary")
    text_files = validate_text_files(root)
    print(
        json.dumps(
            {
                "status": "PASS",
                "manifest_entries": manifest_count,
                "tier_b_rows": tier_b_rows,
                "tier_b_status": tier_b_status,
                "tier_c_rows": tier_c_rows,
                "tier_c_status": tier_c_status,
                "named_rows": named_rows,
                "parquet_rows": parquet_rows,
                "parquet_columns": parquet_columns,
                "atlas_rows": atlas_rows,
                "text_files_lf_checked": text_files,
                "GLOBAL_COLLATZ": "OPEN",
            },
            sort_keys=True,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
