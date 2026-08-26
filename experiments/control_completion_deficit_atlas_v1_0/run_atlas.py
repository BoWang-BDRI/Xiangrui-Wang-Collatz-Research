#!/usr/bin/env python3
"""Build the Control-Completion Deficit Atlas v1.0 finite data products."""

from __future__ import annotations

import argparse
import bisect
import csv
import hashlib
import heapq
import json
import math
import random
import sys
import time
from collections import Counter, defaultdict
from contextlib import ExitStack
from decimal import Decimal, ROUND_CEILING, ROUND_FLOOR, getcontext
from functools import lru_cache
from pathlib import Path
from typing import Any, Iterable, Sequence

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE / "src"))

from control_deficit_core import (  # noqa: E402
    count_windows,
    depth_class,
    encode_depth_factor,
    exact_sanity_failures,
    factor_sets_from_binary,
    first_critical_break,
    longest_factor_match,
    maximal_runs,
    residue_signature_row,
    run_max_length,
    state_features,
    trajectory_states,
)


SUMMARY_FIELDS = [
    "orbit_id",
    "tier",
    "start_n",
    "status",
    "odd_steps_to_1",
    "terminal_or_cap_state",
    "max_odd_value",
    "max_up_burst",
    "max_critical_alphabet_run",
    "max_critical_grammar_run",
    "first_critical_break_type",
    "count_U1",
    "count_F2",
    "count_F3",
    "count_F4P",
    "fraction_mod8_1",
    "fraction_mod8_3",
    "fraction_mod8_5",
    "fraction_mod8_7",
    "max_cum_reset_deficit",
    "min_cum_reset_deficit",
    "final_cum_reset_deficit",
    "max_cum_best_hidden_deficit",
    "final_cum_best_hidden_deficit",
    "height_cocycle_sum",
    "height_cocycle_endpoint_log2",
    "height_cocycle_error",
    "critical_windows_L8",
    "critical_windows_L16",
    "critical_windows_L32",
    "critical_windows_L64",
    "alphabet_windows_L8",
    "alphabet_windows_L16",
    "alphabet_windows_L32",
    "alphabet_windows_L64",
]


NAMED_FIELDS = [
    "orbit_id",
    "start_n",
    "odd_step_index",
    "is_terminal",
    "n",
    "A",
    "B",
    "C",
    "D",
    "a11",
    "a13",
    "a31",
    "a33",
    "n_mod_3",
    "n_mod_4",
    "n_mod_8",
    "n_mod_16",
    "n_mod_32",
    "n_mod_64",
    "actual_mode",
    "actual_next",
    "actual_direction",
    "missing_down_count",
    "missing_up_count",
    "best_hidden_value",
    "best_hidden_mode",
    "reset_value",
    "sheet_alternative",
    "actual_sheet",
    "alternate_sheet",
    "reset_ratio_num",
    "reset_ratio_den",
    "delta_reset_log2",
    "hidden_ratio_num",
    "hidden_ratio_den",
    "delta_hidden_log2",
    "cum_reset_deficit_before",
    "cum_reset_deficit_after",
    "cum_hidden_deficit_before",
    "cum_hidden_deficit_after",
    "height_g",
    "epsilon",
    "eta",
    "cum_height_g",
]


class PriorityReservoir:
    """Keep rows with the smallest deterministic 64-bit hash priorities."""

    def __init__(self, capacity: int, seed: int, namespace: str):
        self.capacity = capacity
        self.seed = seed
        self.namespace = namespace
        self.heap: list[tuple[int, str, Any]] = []

    def add(self, key: str, row: Any) -> None:
        digest = hashlib.blake2b(
            f"{self.seed}|{self.namespace}|{key}".encode("utf-8"), digest_size=8
        ).digest()
        priority = int.from_bytes(digest, "big")
        item = (-priority, key, row)
        if len(self.heap) < self.capacity:
            heapq.heappush(self.heap, item)
        elif priority < -self.heap[0][0]:
            heapq.heapreplace(self.heap, item)

    def rows(self) -> list[Any]:
        return [item[2] for item in sorted(self.heap, key=lambda item: (-item[0], item[1]))]


def write_csv(path: Path, fieldnames: Sequence[str], rows: Iterable[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def generate_sturmian(symbol_count: int) -> tuple[list[int], dict[str, Any]]:
    """Generate depth symbols independently from the upper mechanical word."""
    getcontext().prec = 80
    alpha = Decimal(2).ln() / Decimal(3).ln()
    beta = (Decimal(3) / Decimal(2)).ln() / Decimal(2).ln()

    depths: list[int] = []
    x = Decimal(0)
    previous_ceil = 0
    previous_one_position: int | None = None
    parity_index = 0
    one_count = 0
    while len(depths) < symbol_count:
        x += alpha
        current_ceil = int(x.to_integral_value(rounding=ROUND_CEILING))
        symbol = current_ceil - previous_ceil
        if symbol not in (0, 1):
            raise RuntimeError(f"mechanical word symbol {symbol} at {parity_index}")
        if symbol == 1:
            one_count += 1
            if previous_one_position is not None:
                depths.append(parity_index - previous_one_position)
            previous_one_position = parity_index
        previous_ceil = current_ceil
        parity_index += 1

    candidate: list[int] = []
    y = Decimal(0)
    previous_floor = 0
    for _ in range(symbol_count):
        y += beta
        current_floor = int(y.to_integral_value(rounding=ROUND_FLOOR))
        candidate.append(1 + current_floor - previous_floor)
        previous_floor = current_floor

    mismatches = [index for index, (left, right) in enumerate(zip(depths, candidate)) if left != right]
    if mismatches:
        raise RuntimeError(f"Sturmian candidate formula mismatch at {mismatches[0]}")

    binary = [value - 1 for value in depths]
    count_1 = depths.count(1)
    count_2 = symbol_count - count_1
    max_u = run_max_length(depths, lambda value: value == 1)
    max_f = run_max_length(depths, lambda value: value == 2)
    macros = Counter()
    index = 0
    macro_error: str | None = None
    while index < len(depths):
        if depths[index] != 1:
            macro_error = f"macro does not start U at depth index {index}"
            break
        end = index + 1
        while end < len(depths) and depths[end] == 2:
            end += 1
        block = tuple(depths[index:end])
        if block == (1, 2):
            macros["UF"] += 1
        elif block == (1, 2, 2):
            macros["UFF"] += 1
        elif end == len(depths) and block in ((1,), (1, 2)):
            macros["TRUNCATED_FINAL"] += 1
        else:
            macro_error = f"unexpected macro {block[:8]} at depth index {index}"
            break
        index = end

    metadata = {
        "alpha_decimal_80": str(alpha),
        "beta_decimal_80": str(beta),
        "odd_return_symbol_count": symbol_count,
        "parity_symbols_consumed": parity_index,
        "parity_ones_consumed": one_count,
        "candidate_formula_mismatches": 0,
        "indexing_correction": "NONE; zero-based i matches the stated candidate formula",
        "count_a1": count_1,
        "count_a2": count_2,
        "frequency_a1": count_1 / symbol_count,
        "frequency_a2": count_2 / symbol_count,
        "alphabet_subset_1_2": set(depths) <= {1, 2},
        "no_consecutive_a1": max_u == 1,
        "max_U_run": max_u,
        "max_F_run": max_f,
        "macro_counts": dict(macros),
        "macro_error": macro_error,
        "mod8_translation": {
            "F2": "n == 1 (mod 8)",
            "U1_without_UU": "n == 3 (mod 8)",
            "deleted_deep_fold_port_n_mod8_5": True,
            "deleted_repeated_UP_port_n_mod8_7": True,
        },
        "positive_natural_source_claimed": False,
    }
    return binary, metadata


def summary_for_orbit(
    orbit_id: str,
    tier: str,
    start: int,
    states: Sequence[int],
    status: str,
    terminal: int,
    factor_sets: dict[int, set[int]],
    critical_lengths: Sequence[int],
) -> tuple[dict[str, Any], dict[str, Any]]:
    features = [cached_features(n) for n in states]
    depths = [feature.a31 for feature in features]
    deltas_r = [feature.delta_reset_log2 for feature in features]
    deltas_h = [feature.delta_hidden_log2 for feature in features]
    g_values = [feature.height_g for feature in features]

    cumulative_r = [0.0]
    cumulative_h = [0.0]
    for delta_r, delta_h in zip(deltas_r, deltas_h):
        cumulative_r.append(cumulative_r[-1] + delta_r)
        cumulative_h.append(cumulative_h[-1] + delta_h)

    counts = Counter(depth_class(depth) for depth in depths)
    residues = Counter(n % 8 for n in states)
    windows = count_windows(depths, critical_lengths, factor_sets)
    endpoint_log = math.log2(terminal) - math.log2(start)
    g_sum = math.fsum(g_values)
    row: dict[str, Any] = {
        "orbit_id": orbit_id,
        "tier": tier,
        "start_n": start,
        "status": status,
        "odd_steps_to_1": len(states) if status == "REACHED_1" else "",
        "terminal_or_cap_state": terminal,
        "max_odd_value": max([start, terminal, *states]),
        "max_up_burst": run_max_length(depths, lambda depth: depth == 1),
        "max_critical_alphabet_run": run_max_length(depths, lambda depth: depth in (1, 2)),
        "max_critical_grammar_run": longest_factor_match(depths, factor_sets),
        "first_critical_break_type": first_critical_break(depths, factor_sets),
        "count_U1": counts["U1"],
        "count_F2": counts["F2"],
        "count_F3": counts["F3"],
        "count_F4P": counts["F4P"],
        "fraction_mod8_1": residues[1] / len(states) if states else 0.0,
        "fraction_mod8_3": residues[3] / len(states) if states else 0.0,
        "fraction_mod8_5": residues[5] / len(states) if states else 0.0,
        "fraction_mod8_7": residues[7] / len(states) if states else 0.0,
        "max_cum_reset_deficit": max(cumulative_r),
        "min_cum_reset_deficit": min(cumulative_r),
        "final_cum_reset_deficit": cumulative_r[-1],
        "max_cum_best_hidden_deficit": max(cumulative_h),
        "final_cum_best_hidden_deficit": cumulative_h[-1],
        "height_cocycle_sum": g_sum,
        "height_cocycle_endpoint_log2": endpoint_log,
        "height_cocycle_error": g_sum - endpoint_log,
    }
    for length in critical_lengths:
        total, alphabet, critical = windows[length]
        row[f"critical_windows_L{length}"] = critical
        row[f"alphabet_windows_L{length}"] = alphabet
        row[f"total_windows_L{length}"] = total

    details = {
        "features": features,
        "depths": depths,
        "deltas_r": deltas_r,
        "deltas_h": deltas_h,
        "g_values": g_values,
        "cumulative_r": cumulative_r,
        "cumulative_h": cumulative_h,
        "windows": windows,
    }
    return row, details


@lru_cache(maxsize=300_000)
def cached_features(n: int):
    return state_features(n)


def named_state_rows(
    orbit_id: str,
    start: int,
    states: Sequence[int],
    details: dict[str, Any],
) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    cum_g = 0.0
    for index, feature in enumerate(details["features"]):
        cum_g += feature.height_g
        rows.append(
            {
                "orbit_id": orbit_id,
                "start_n": start,
                "odd_step_index": index,
                "is_terminal": 0,
                "n": feature.n,
                "A": feature.A,
                "B": feature.B,
                "C": feature.C,
                "D": feature.D,
                "a11": feature.a11,
                "a13": feature.a13,
                "a31": feature.a31,
                "a33": feature.a33,
                "n_mod_3": feature.n % 3,
                "n_mod_4": feature.n % 4,
                "n_mod_8": feature.n % 8,
                "n_mod_16": feature.n % 16,
                "n_mod_32": feature.n % 32,
                "n_mod_64": feature.n % 64,
                "actual_mode": "(3,1)",
                "actual_next": feature.C,
                "actual_direction": feature.actual_direction,
                "missing_down_count": feature.missing_down_count,
                "missing_up_count": feature.missing_up_count,
                "best_hidden_value": feature.best_hidden_value,
                "best_hidden_mode": feature.best_hidden_mode,
                "reset_value": feature.A,
                "sheet_alternative": feature.D,
                "actual_sheet": "NON3",
                "alternate_sheet": "MULT3",
                "reset_ratio_num": feature.C,
                "reset_ratio_den": feature.A,
                "delta_reset_log2": feature.delta_reset_log2,
                "hidden_ratio_num": feature.C,
                "hidden_ratio_den": feature.best_hidden_value,
                "delta_hidden_log2": feature.delta_hidden_log2,
                "cum_reset_deficit_before": details["cumulative_r"][index],
                "cum_reset_deficit_after": details["cumulative_r"][index + 1],
                "cum_hidden_deficit_before": details["cumulative_h"][index],
                "cum_hidden_deficit_after": details["cumulative_h"][index + 1],
                "height_g": feature.height_g,
                "epsilon": feature.epsilon,
                "eta": feature.eta,
                "cum_height_g": cum_g,
            }
        )

    terminal = cached_features(1)
    rows.append(
        {
            "orbit_id": orbit_id,
            "start_n": start,
            "odd_step_index": len(states),
            "is_terminal": 1,
            "n": 1,
            "A": terminal.A,
            "B": terminal.B,
            "C": terminal.C,
            "D": terminal.D,
            "a11": terminal.a11,
            "a13": terminal.a13,
            "a31": terminal.a31,
            "a33": terminal.a33,
            "n_mod_3": 1,
            "n_mod_4": 1,
            "n_mod_8": 1,
            "n_mod_16": 1,
            "n_mod_32": 1,
            "n_mod_64": 1,
            "actual_mode": "(3,1)",
            "actual_next": 1,
            "actual_direction": "BOUNDARY",
            "missing_down_count": terminal.missing_down_count,
            "missing_up_count": terminal.missing_up_count,
            "best_hidden_value": terminal.best_hidden_value,
            "best_hidden_mode": terminal.best_hidden_mode,
            "reset_value": terminal.A,
            "sheet_alternative": terminal.D,
            "actual_sheet": "NON3",
            "alternate_sheet": "MULT3",
            "reset_ratio_num": 1,
            "reset_ratio_den": 1,
            "delta_reset_log2": 0.0,
            "hidden_ratio_num": 1,
            "hidden_ratio_den": 1,
            "delta_hidden_log2": 0.0,
            "cum_reset_deficit_before": details["cumulative_r"][-1],
            "cum_reset_deficit_after": details["cumulative_r"][-1],
            "cum_hidden_deficit_before": details["cumulative_h"][-1],
            "cum_hidden_deficit_after": details["cumulative_h"][-1],
            "height_g": 0.0,
            "epsilon": 0.0,
            "eta": 0.0,
            "cum_height_g": cum_g,
        }
    )
    return rows


def state_sample_row(orbit: dict[str, Any], index: int) -> dict[str, Any]:
    feature = orbit["details"]["features"][index]
    return {
        "orbit_id": orbit["orbit_id"],
        "tier": orbit["tier"],
        "start_n_exact_decimal": str(orbit["start"]),
        "odd_step_index": index,
        "n_exact_decimal": str(feature.n),
        "A_exact_decimal": str(feature.A),
        "B_exact_decimal": str(feature.B),
        "C_exact_decimal": str(feature.C),
        "D_exact_decimal": str(feature.D),
        "a11": feature.a11,
        "a13": feature.a13,
        "a31": feature.a31,
        "a33": feature.a33,
        "n_mod_3": feature.n % 3,
        "n_mod_4": feature.n % 4,
        "n_mod_8": feature.n % 8,
        "n_mod_16": feature.n % 16,
        "n_mod_32": feature.n % 32,
        "n_mod_64": feature.n % 64,
        "actual_next_exact_decimal": str(feature.C),
        "actual_direction": feature.actual_direction,
        "missing_down_count": feature.missing_down_count,
        "missing_up_count": feature.missing_up_count,
        "best_hidden_value_exact_decimal": str(feature.best_hidden_value),
        "best_hidden_mode": feature.best_hidden_mode,
        "reset_ratio_num_exact_decimal": str(feature.C),
        "reset_ratio_den_exact_decimal": str(feature.A),
        "delta_reset_log2": feature.delta_reset_log2,
        "hidden_ratio_num_exact_decimal": str(feature.C),
        "hidden_ratio_den_exact_decimal": str(feature.best_hidden_value),
        "delta_hidden_log2": feature.delta_hidden_log2,
        "height_g": feature.height_g,
        "epsilon": feature.epsilon,
        "eta": feature.eta,
    }


def build_runs(orbit: dict[str, Any]) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    states = orbit["states"]
    depths = orbit["details"]["depths"]
    delta_r = orbit["details"]["deltas_r"]
    delta_h = orbit["details"]["deltas_h"]
    for run_type, predicate in (
        ("U1", lambda value: value == 1),
        ("CRITICAL_ALPHABET_1_2", lambda value: value in (1, 2)),
    ):
        for start, end in maximal_runs(depths, predicate):
            rows.append(
                {
                    "orbit_id": orbit["orbit_id"],
                    "tier": orbit["tier"],
                    "start_n": orbit["start"],
                    "run_type": run_type,
                    "start_index": start,
                    "end_index": end,
                    "start_state": states[start],
                    "end_state": states[end],
                    "length": end - start + 1,
                    "max_state": max(states[start : end + 1]),
                    "delta_cumulative_reset_deficit": math.fsum(delta_r[start : end + 1]),
                    "delta_cumulative_best_hidden_deficit": math.fsum(delta_h[start : end + 1]),
                }
            )
    return rows


def build_event_rows(orbit: dict[str, Any], windows: Sequence[int]) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    compensation: list[dict[str, Any]] = []
    peaks: list[dict[str, Any]] = []
    states = orbit["states"]
    details = orbit["details"]
    depths = details["depths"]
    deltas = details["deltas_r"]
    cumulative = details["cumulative_r"]

    for index, depth in enumerate(depths):
        if depth >= 3:
            feature = details["features"][index]
            row = {
                "orbit_id": orbit["orbit_id"],
                "tier": orbit["tier"],
                "start_n": orbit["start"],
                "fold_index": index,
                "fold_state": states[index],
                "prior_D_R": cumulative[index],
                "fold_depth": depth,
                "delta_reset_at_fold": deltas[index],
            }
            for width in windows:
                row[f"prior_Q{width}"] = math.fsum(deltas[index - width : index]) if index >= width else ""
            for modulus in (8, 16, 32, 64, 128, 256):
                row[f"n_mod_{modulus}"] = states[index] % modulus
            compensation.append(row)

    running_peak = 0.0
    for index, after in enumerate(cumulative[1:]):
        if after <= running_peak:
            continue
        pre_level = cumulative[index]
        running_peak = after
        next3 = next((future - index for future in range(index + 1, len(depths)) if depths[future] >= 3), None)
        next4 = next((future - index for future in range(index + 1, len(depths)) if depths[future] >= 4), None)
        repayment_index = next(
            (future for future in range(index + 1, len(depths)) if cumulative[future + 1] <= pre_level),
            None,
        )
        end = repayment_index if repayment_index is not None else len(states) - 1
        segment_states = states[index : end + 1]
        segment_depths = depths[index : end + 1]
        peaks.append(
            {
                "orbit_id": orbit["orbit_id"],
                "tier": orbit["tier"],
                "start_n": orbit["start"],
                "peak_index": index,
                "peak_state": states[index],
                "pre_peak_level": pre_level,
                "peak_debt": after,
                "steps_to_next_a31_ge_3": next3 if next3 is not None else "CENSORED",
                "steps_to_next_a31_ge_4": next4 if next4 is not None else "CENSORED",
                "steps_until_D_R_returns_below_pre_peak_level": (
                    repayment_index - index if repayment_index is not None else "CENSORED"
                ),
                "repayment_status": "REPAID" if repayment_index is not None else "CENSORED",
                "max_state_before_repayment": max(segment_states) if segment_states else states[index],
                "max_a31_before_repayment": max(segment_depths) if segment_depths else depths[index],
            }
        )
    return compensation, peaks


def quantile_edges(values: Sequence[float], bins: int = 10) -> list[float]:
    ordered = sorted(values)
    if not ordered:
        return []
    return [ordered[min(len(ordered) - 1, math.ceil(len(ordered) * q / bins) - 1)] for q in range(1, bins)]


def h1_rows(
    analysis_orbits: Sequence[dict[str, Any]],
    windows: Sequence[int],
    capacity: int,
    seed: int,
) -> list[dict[str, Any]]:
    output: list[dict[str, Any]] = []
    global_depths = [depth for orbit in analysis_orbits for depth in orbit["details"]["depths"]]
    rng = random.Random(seed ^ 0xA31D3)
    shuffled_within: dict[str, list[int]] = {}
    for orbit in analysis_orbits:
        values = list(orbit["details"]["depths"])
        rng.shuffle(values)
        shuffled_within[orbit["orbit_id"]] = values
    orbit_order = list(analysis_orbits)
    permuted = list(analysis_orbits)
    rng.shuffle(permuted)
    segment_map = {left["orbit_id"]: right for left, right in zip(orbit_order, permuted)}

    for width in windows:
        reservoir = PriorityReservoir(capacity, seed, f"H1_W{width}")
        for orbit in analysis_orbits:
            depths = orbit["details"]["depths"]
            deltas = orbit["details"]["deltas_r"]
            rolling = math.fsum(deltas[:width]) if len(deltas) >= width else 0.0
            for index in range(width, len(depths)):
                if index > width:
                    rolling += deltas[index - 1] - deltas[index - width - 1]
                reservoir.add(
                    f"{orbit['orbit_id']}|{index}",
                    (orbit["orbit_id"], index, rolling, depths[index]),
                )
        records = reservoir.rows()
        edges = quantile_edges([record[2] for record in records])
        controls: dict[str, list[int]] = {"ACTUAL": [record[3] for record in records]}
        controls["WITHIN_ORBIT_SHUFFLE"] = [
            shuffled_within[orbit_id][index] for orbit_id, index, _, _ in records
        ]
        segment_values: list[int] = []
        for orbit_id, index, _, _ in records:
            source = segment_map[orbit_id]["details"]["depths"]
            segment_values.append(source[index % len(source)] if source else 1)
        controls["SHUFFLED_ORBIT_SEGMENTS"] = segment_values
        controls["SYNTHETIC_IID_MARGINAL"] = [rng.choice(global_depths) for _ in records]

        for control_name, outcomes in controls.items():
            grouped: list[list[int]] = [[] for _ in range(10)]
            for record, outcome in zip(records, outcomes):
                grouped[bisect.bisect_right(edges, record[2])].append(outcome)
            for quantile, group in enumerate(grouped, start=1):
                output.append(
                    {
                        "hypothesis": "H1_DEBT_COMPENSATION_ASSOCIATION",
                        "test": "RESET_DEBT_WINDOW_QUANTILE",
                        "control": control_name,
                        "parameter": f"W={width};Q={quantile}",
                        "n": len(group),
                        "statistic": "conditional_depth_metrics",
                        "value": math.fsum(group) / len(group) if group else "",
                        "p_a31_ge_3": sum(value >= 3 for value in group) / len(group) if group else "",
                        "p_a31_ge_4": sum(value >= 4 for value in group) / len(group) if group else "",
                        "p_a31_ge_5": sum(value >= 5 for value in group) / len(group) if group else "",
                        "quantile_upper_edge": edges[quantile - 1] if quantile <= 9 else "INF",
                        "interpretation": "EXPERIMENTAL_ASSOCIATION_NOT_CAUSATION",
                    }
                )
    return output


def rolling_code_set(binary: Sequence[int], length: int) -> set[int]:
    if len(binary) < length:
        return set()
    mask = (1 << length) - 1
    code = 0
    result: set[int] = set()
    for index, bit in enumerate(binary):
        code = ((code << 1) | bit) & mask
        if index + 1 >= length:
            result.add(code)
    return result


def write_parquet(path: Path, rows: Sequence[dict[str, Any]]) -> None:
    try:
        import pyarrow as pa
        import pyarrow.parquet as pq
    except ImportError as exc:
        raise RuntimeError("pyarrow is required for state_sample.parquet") from exc
    table = pa.Table.from_pylist(list(rows))
    pq.write_table(table, path, compression="zstd", version="2.6")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=HERE / "config.json")
    parser.add_argument("--output", type=Path, default=HERE / "outputs")
    parser.add_argument("--smoke", action="store_true")
    args = parser.parse_args()
    config = json.loads(args.config.read_text(encoding="utf-8"))
    output = args.output.resolve()
    output.mkdir(parents=True, exist_ok=True)
    started = time.time()

    if args.smoke:
        config["tier_b_max_inclusive"] = 9999
        config["tier_c_count"] = 200
        config["sturmian_odd_return_symbols"] = 10000
        config["analysis_cohort_per_tier"] = 64
        config["state_sample_capacity"] = 1000
        config["h1_sample_capacity_per_window"] = 1000

    seed = int(config["public_seed"])
    windows = [int(value) for value in config["windows"]]
    critical_lengths = [int(value) for value in config["critical_window_lengths"]]

    # Sturmian symbolic skeleton and language.
    sturmian_binary, sturmian_meta = generate_sturmian(int(config["sturmian_odd_return_symbols"]))
    factor_sets = factor_sets_from_binary(sturmian_binary, int(config["sturmian_factor_max_length"]))
    complexity = {length: len(factors) for length, factors in factor_sets.items()}
    bad_complexity = {length: count for length, count in complexity.items() if count != length + 1}
    if bad_complexity:
        raise RuntimeError(f"Sturmian factor complexity failure: {bad_complexity}")
    sturmian_meta["factor_complexity"] = complexity
    sturmian_meta["factor_complexity_L_plus_1"] = True

    factor_rows: list[dict[str, Any]] = []
    for length, factors in factor_sets.items():
        if length <= 16:
            universe = range(1 << length)
            for code in universe:
                factor_rows.append(
                    {
                        "length": length,
                        "factor": "".join("2" if bit == "1" else "1" for bit in f"{code:0{length}b}"),
                        "status": "PRESENT" if code in factors else "FORBIDDEN",
                    }
                )
        else:
            for code in sorted(factors):
                factor_rows.append(
                    {
                        "length": length,
                        "factor": "".join("2" if bit == "1" else "1" for bit in f"{code:0{length}b}"),
                        "status": "PRESENT",
                    }
                )
    write_csv(output / "sturmian_factors.csv", ["length", "factor", "status"], factor_rows)
    (output / "sturmian_summary.json").write_text(
        json.dumps(sturmian_meta, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
    )

    # Exact sanity checks across the entire Tier B input domain.
    tier_b_max = int(config["tier_b_max_inclusive"])
    sanity_failures: list[dict[str, Any]] = []
    for n in range(1, tier_b_max + 1, 2):
        failures = exact_sanity_failures(n)
        if failures:
            sanity_failures.append({"n": n, "failures": failures})
            break
    if sanity_failures:
        raise RuntimeError(f"FATAL exact sanity failure: {sanity_failures[0]}")
    sanity = {
        "tested_odd_n": (tier_b_max + 1) // 2,
        "range": [1, tier_b_max],
        "n_gt_3_quantifier_respected": True,
        "boundary_1_3_separate": True,
        "failures": 0,
        "status": "PASS_EXACT_FINITE_DOMAIN",
    }
    (output / "sanity_checks.json").write_text(
        json.dumps(sanity, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
    )

    rng_b = random.Random(seed ^ 0xB)
    tier_b_population = range(1, tier_b_max + 1, 2)
    cohort_count_b = min(int(config["analysis_cohort_per_tier"]), len(tier_b_population))
    cohort_b = set(rng_b.sample(tier_b_population, cohort_count_b))

    rng_c = random.Random(seed ^ 0xC)
    tier_c_population = range(1, int(config["tier_c_max_inclusive"]) + 1, 2)
    tier_c_starts = rng_c.sample(tier_c_population, int(config["tier_c_count"]))
    cohort_c = set(tier_c_starts[: min(int(config["analysis_cohort_per_tier"]), len(tier_c_starts))])

    next_cache: dict[int, int] = {}
    analysis_orbits: list[dict[str, Any]] = []
    named_rows: list[dict[str, Any]] = []
    named_summaries: list[dict[str, Any]] = []
    top_heaps: dict[str, list[tuple[float, int, dict[str, Any]]]] = {
        metric: []
        for metric in (
            "max_odd_value",
            "max_up_burst",
            "max_critical_alphabet_run",
            "max_critical_grammar_run",
            "max_cum_reset_deficit",
        )
    }
    break_counts_b: Counter[str] = Counter()
    h3: dict[tuple[int, int], list[float]] = defaultdict(lambda: [0.0, 0.0, 0.0])
    h5: Counter[tuple[int, int, int, str]] = Counter()
    max_cocycle_error = 0.0

    # Tier A named complete orbits.
    for start in config["named_starts"]:
        orbit_id = f"NAMED_{start}"
        states, status, terminal = trajectory_states(int(start), int(config["tier_b_step_cap"]), next_cache)
        row, details = summary_for_orbit(
            orbit_id, "TIER_A_NAMED", int(start), states, status, terminal, factor_sets, critical_lengths
        )
        if status != "REACHED_1":
            raise RuntimeError(f"named orbit {start} did not reach 1: {status}")
        named_summaries.append(row)
        named_rows.extend(named_state_rows(orbit_id, int(start), states, details))
        analysis_orbits.append(
            {"orbit_id": orbit_id, "tier": "TIER_A_NAMED", "start": int(start), "states": states, "details": details}
        )
    write_csv(output / "named_orbits.csv", NAMED_FIELDS, named_rows)

    # Tier B complete odd-start scan.
    tier_b_part_paths = [
        output / "orbit_summary_1e6_part01_of_02.csv",
        output / "orbit_summary_1e6_part02_of_02.csv",
    ]
    tier_b_split_after = len(tier_b_population) // 2
    with ExitStack() as stack:
        writers = []
        for part_path in tier_b_part_paths:
            handle = stack.enter_context(part_path.open("w", encoding="utf-8", newline=""))
            part_writer = csv.DictWriter(
                handle, fieldnames=SUMMARY_FIELDS, lineterminator="\n", extrasaction="ignore"
            )
            part_writer.writeheader()
            writers.append(part_writer)
        for ordinal, start in enumerate(tier_b_population, start=1):
            orbit_id = f"B_{start}"
            states, status, terminal = trajectory_states(start, int(config["tier_b_step_cap"]), next_cache)
            row, details = summary_for_orbit(
                orbit_id, "TIER_B_1E6", start, states, status, terminal, factor_sets, critical_lengths
            )
            writers[0 if ordinal <= tier_b_split_after else 1].writerow(row)
            max_cocycle_error = max(max_cocycle_error, abs(float(row["height_cocycle_error"])))
            break_counts_b[str(row["first_critical_break_type"])] += 1
            for metric, heap in top_heaps.items():
                value = float(row[metric])
                item = (value, start, dict(row))
                if len(heap) < 100:
                    heapq.heappush(heap, item)
                elif item[:2] > heap[0][:2]:
                    heapq.heapreplace(heap, item)

            features = details["features"]
            for index, feature in enumerate(features):
                if feature.a31 >= 3:
                    repayment = -feature.delta_reset_log2
                    for bits in range(3, 9):
                        key = (bits, feature.n % (1 << bits))
                        accumulator = h3[key]
                        accumulator[0] += 1
                        accumulator[1] += repayment
                        accumulator[2] += repayment * repayment
                for modulus in (3, 9, 27, 81):
                    h5[(modulus, feature.n % modulus, feature.C % modulus, depth_class(feature.a31))] += 1

            if start in cohort_b:
                analysis_orbits.append(
                    {"orbit_id": orbit_id, "tier": "TIER_B_1E6", "start": start, "states": states, "details": details}
                )
            if ordinal % 100_000 == 0:
                print(f"tier_b_completed={ordinal}", flush=True)

    # Tier C deterministic large-integer sample.
    tier_c_rows: list[dict[str, Any]] = []
    tier_c_status = Counter()
    for ordinal, start in enumerate(tier_c_starts, start=1):
        orbit_id = f"C_{ordinal:05d}"
        states, status, terminal = trajectory_states(start, int(config["tier_c_step_cap"]), next_cache)
        row, details = summary_for_orbit(
            orbit_id, "TIER_C_RANDOM_1E12", start, states, status, terminal, factor_sets, critical_lengths
        )
        tier_c_rows.append(row)
        tier_c_status[status] += 1
        max_cocycle_error = max(max_cocycle_error, abs(float(row["height_cocycle_error"])))
        if start in cohort_c:
            analysis_orbits.append(
                {"orbit_id": orbit_id, "tier": "TIER_C_RANDOM_1E12", "start": start, "states": states, "details": details}
            )
    write_csv(output / "orbit_summary_tier_c.csv", SUMMARY_FIELDS, tier_c_rows)

    # Deterministic state sample and detailed cohort events.
    state_reservoir = PriorityReservoir(int(config["state_sample_capacity"]), seed, "STATE_SAMPLE")
    run_rows: list[dict[str, Any]] = []
    compensation_rows: list[dict[str, Any]] = []
    peak_rows: list[dict[str, Any]] = []
    for orbit in analysis_orbits:
        for index in range(len(orbit["states"])):
            state_reservoir.add(
                f"{orbit['orbit_id']}|{index}", state_sample_row(orbit, index)
            )
        run_rows.extend(build_runs(orbit))
        compensation, peaks = build_event_rows(orbit, windows)
        compensation_rows.extend(compensation)
        peak_rows.extend(peaks)
    state_sample_rows = state_reservoir.rows()
    write_parquet(output / "state_sample.parquet", state_sample_rows)
    write_csv(
        output / "passive_runs.csv",
        [
            "orbit_id", "tier", "start_n", "run_type", "start_index", "end_index",
            "start_state", "end_state", "length", "max_state",
            "delta_cumulative_reset_deficit", "delta_cumulative_best_hidden_deficit",
        ],
        run_rows,
    )
    compensation_fields = [
        "orbit_id", "tier", "start_n", "fold_index", "fold_state", "prior_D_R",
        *[f"prior_Q{width}" for width in windows],
        "fold_depth", "delta_reset_at_fold",
        *[f"n_mod_{modulus}" for modulus in (8, 16, 32, 64, 128, 256)],
    ]
    write_csv(output / "compensation_events.csv", compensation_fields, compensation_rows)
    write_csv(
        output / "debt_peak_events.csv",
        [
            "orbit_id", "tier", "start_n", "peak_index", "peak_state", "pre_peak_level",
            "peak_debt", "steps_to_next_a31_ge_3", "steps_to_next_a31_ge_4",
            "steps_until_D_R_returns_below_pre_peak_level", "repayment_status",
            "max_state_before_repayment", "max_a31_before_repayment",
        ],
        peak_rows,
    )

    # Natural-vs-Sturmian named rows, aggregate, and top 100 Tier B records.
    natural_rows: list[dict[str, Any]] = []
    for row in named_summaries:
        for length in critical_lengths:
            natural_rows.append(
                {
                    "scope": row["orbit_id"],
                    "start_n": row["start_n"],
                    "length": length,
                    "total_windows": row[f"total_windows_L{length}"],
                    "alphabet_1_2_windows": row[f"alphabet_windows_L{length}"],
                    "critical_sturmian_windows": row[f"critical_windows_L{length}"],
                    "sturmian_complexity": complexity[length],
                    "max_critical_alphabet_run": row["max_critical_alphabet_run"],
                    "max_critical_grammar_run": row["max_critical_grammar_run"],
                    "first_break_type": row["first_critical_break_type"],
                }
            )

    top_critical = sorted(top_heaps["max_critical_grammar_run"], reverse=True)
    for _, _, row in top_critical:
        for length in critical_lengths:
            natural_rows.append(
                {
                    "scope": "TIER_B_TOP100_CRITICAL_LIKE",
                    "start_n": row["start_n"],
                    "length": length,
                    "total_windows": row[f"total_windows_L{length}"],
                    "alphabet_1_2_windows": row[f"alphabet_windows_L{length}"],
                    "critical_sturmian_windows": row[f"critical_windows_L{length}"],
                    "sturmian_complexity": complexity[length],
                    "max_critical_alphabet_run": row["max_critical_alphabet_run"],
                    "max_critical_grammar_run": row["max_critical_grammar_run"],
                    "first_break_type": row["first_critical_break_type"],
                }
            )
    write_csv(
        output / "natural_vs_sturmian.csv",
        [
            "scope", "start_n", "length", "total_windows", "alphabet_1_2_windows",
            "critical_sturmian_windows", "sturmian_complexity", "max_critical_alphabet_run",
            "max_critical_grammar_run", "first_break_type",
        ],
        natural_rows,
    )

    # Exact residue signature atlas.
    atlas_rows = [
        residue_signature_row(int(math.log2(modulus)), residue)
        for modulus in config["residue_moduli"]
        for residue in range(1, modulus, 2)
    ]
    write_csv(
        output / "residue_signature_atlas.csv",
        [
            "modulus", "bits", "odd_residue", "a11", "a13", "a31", "a33",
            "coarse_signature", "output_ordering", "actual_C_direction", "best_hidden_mode",
            "missing_down_count", "missing_up_count", "D_sheet_switching_ability",
        ],
        atlas_rows,
    )

    # H1 and required negative controls.
    hypothesis_rows = h1_rows(
        analysis_orbits, windows, int(config["h1_sample_capacity_per_window"]), seed
    )

    # H2/H4: compare the critical word with a same-frequency random balanced word.
    balanced = list(sturmian_binary)
    random.Random(seed ^ 0xBA1A).shuffle(balanced)
    alphabet_window_reservoirs = {
        length: PriorityReservoir(100_000, seed, f"NATURAL_WINDOW_L{length}")
        for length in critical_lengths
    }
    for orbit in analysis_orbits:
        depths = orbit["details"]["depths"]
        for length in critical_lengths:
            for index in range(0, max(0, len(depths) - length + 1)):
                code = encode_depth_factor(depths[index : index + length])
                if code is not None:
                    alphabet_window_reservoirs[length].add(
                        f"{orbit['orbit_id']}|{index}", code
                    )
    for length in critical_lengths:
        codes = alphabet_window_reservoirs[length].rows()
        random_factors = rolling_code_set(balanced, length)
        actual_rate = sum(code in factor_sets[length] for code in codes) / len(codes) if codes else 0.0
        random_rate = sum(code in random_factors for code in codes) / len(codes) if codes else 0.0
        hypothesis_rows.append(
            {
                "hypothesis": "H2_CRITICAL_LIKE_RUN_FRAGILITY",
                "test": "STURMIAN_VS_RANDOM_BALANCED_LANGUAGE",
                "control": "SAME_FREQUENCY_RANDOM_BALANCED_WORD",
                "parameter": f"L={length}",
                "n": len(codes),
                "statistic": "natural_alphabet_window_membership",
                "value": actual_rate,
                "control_value": random_rate,
                "interpretation": "FINITE_LANGUAGE_COMPARISON",
            }
        )
        hypothesis_rows.append(
            {
                "hypothesis": "H4_FINITE_ALPHABET_PRESSURE",
                "test": "FACTOR_COMPLEXITY",
                "control": "SAME_FREQUENCY_RANDOM_BALANCED_WORD",
                "parameter": f"L={length}",
                "n": len(sturmian_binary) - length + 1,
                "statistic": "unique_factor_count",
                "value": len(factor_sets[length]),
                "control_value": len(random_factors),
                "interpretation": "SYMBOLIC_SKELETON_ONLY_NOT_PERIODICITY",
            }
        )
        del random_factors

    # H3 dyadic repayment cylinders.
    for (bits, residue), values in sorted(h3.items()):
        count, total, total_sq = values
        mean = total / count
        variance = max(0.0, total_sq / count - mean * mean)
        hypothesis_rows.append(
            {
                "hypothesis": "H3_DEEP_FOLD_RESIDUE_CYLINDERS",
                "test": "DEEP_FOLD_REPAYMENT_BY_DYADIC_CYLINDER",
                "control": "NONE_DESCRIPTIVE",
                "parameter": f"mod={1 << bits};residue={residue}",
                "n": int(count),
                "statistic": "mean_negative_delta_reset",
                "value": mean,
                "variance": variance,
                "interpretation": "FINITE_EXACT_CYLINDER_AGGREGATE_WITH_FLOAT_LOG",
            }
        )

    # H5 exact residue movement grammar counts.
    for (modulus, source, target, grammar), count in sorted(h5.items()):
        hypothesis_rows.append(
            {
                "hypothesis": "H5_SHEET_LOSS_COMPENSATION",
                "test": "PASSIVE_RESIDUE_MOVEMENT_GRAMMAR",
                "control": "NONE_DESCRIPTIVE",
                "parameter": f"mod={modulus};{source}->{target};{grammar}",
                "n": count,
                "statistic": "transition_count",
                "value": count,
                "interpretation": "FINITE_OBSERVATION_NOT_SHEET_RECOVERY",
            }
        )

    hypothesis_fields = sorted({key for row in hypothesis_rows for key in row})
    preferred = [
        "hypothesis", "test", "control", "parameter", "n", "statistic", "value",
        "control_value", "p_a31_ge_3", "p_a31_ge_4", "p_a31_ge_5",
        "quantile_upper_edge", "variance", "interpretation",
    ]
    hypothesis_fields = preferred + [field for field in hypothesis_fields if field not in preferred]
    write_csv(output / "hypothesis_tests.csv", hypothesis_fields, hypothesis_rows)

    # Record cases from all configured rankings.
    record_rows: list[dict[str, Any]] = []
    for metric, heap in top_heaps.items():
        for rank, (value, start, row) in enumerate(sorted(heap, reverse=True), start=1):
            record_rows.append(
                {
                    "metric": metric,
                    "rank": rank,
                    "start_n": start,
                    "value": value,
                    "status": row["status"],
                    "odd_steps_to_1": row["odd_steps_to_1"],
                    "max_odd_value": row["max_odd_value"],
                    "max_up_burst": row["max_up_burst"],
                    "max_critical_alphabet_run": row["max_critical_alphabet_run"],
                    "max_critical_grammar_run": row["max_critical_grammar_run"],
                    "first_break_type": row["first_critical_break_type"],
                }
            )
    write_csv(
        output / "record_cases.csv",
        [
            "metric", "rank", "start_n", "value", "status", "odd_steps_to_1",
            "max_odd_value", "max_up_burst", "max_critical_alphabet_run",
            "max_critical_grammar_run", "first_break_type",
        ],
        record_rows,
    )

    run_summary = {
        "status": "FINITE_EXPERIMENT_COMPLETE" if not args.smoke else "SMOKE_COMPLETE",
        "public_seed": seed,
        "config": config,
        "tier_b_start_count": len(tier_b_population),
        "tier_c_start_count": len(tier_c_starts),
        "tier_c_status_counts": dict(tier_c_status),
        "analysis_orbit_count": len(analysis_orbits),
        "state_sample_rows": len(state_sample_rows),
        "compensation_event_rows": len(compensation_rows),
        "debt_peak_event_rows": len(peak_rows),
        "passive_run_rows": len(run_rows),
        "max_abs_height_cocycle_error": max_cocycle_error,
        "tier_b_first_break_counts": dict(break_counts_b),
        "transition_cache_entries": len(next_cache),
        "feature_cache": cached_features.cache_info()._asdict(),
        "elapsed_seconds": time.time() - started,
        "global_collatz": "OPEN",
        "numerical_evidence_is_proof": False,
    }
    (output / "run_summary.json").write_text(
        json.dumps(run_summary, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n"
    )
    print(json.dumps(run_summary, sort_keys=True), flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
