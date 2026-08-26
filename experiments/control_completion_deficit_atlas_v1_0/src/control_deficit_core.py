"""Exact arithmetic core for the Control-Completion Deficit Atlas.

The dynamical domain is the positive odd integers.  Floating-point values are
used only for explicitly labelled logarithmic diagnostics; all maps, ratios,
valuations, residues, and orbit transitions are exact integers.
"""

from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Iterator, Sequence


MODE_ORDER = ("A", "B", "C", "D")
HIDDEN_MODE_ORDER = ("A", "B", "D")


def v2(value: int) -> int:
    if value <= 0:
        raise ValueError("v2 is restricted to positive integers")
    return (value & -value).bit_length() - 1


def oddpart(value: int) -> int:
    return value >> v2(value)


def direction(value: int, baseline: int) -> str:
    if value > baseline:
        return "UP"
    if value < baseline:
        return "FOLD"
    return "BOUNDARY"


def depth_class(depth: int) -> str:
    if depth == 1:
        return "U1"
    if depth == 2:
        return "F2"
    if depth == 3:
        return "F3"
    return "F4P"


@dataclass(frozen=True, slots=True)
class StateFeatures:
    n: int
    A: int
    B: int
    C: int
    D: int
    a11: int
    a13: int
    a31: int
    a33: int

    @property
    def actual_next(self) -> int:
        return self.C

    @property
    def actual_direction(self) -> str:
        return direction(self.C, self.n)

    @property
    def missing_down_count(self) -> int:
        return sum(value < self.n for value in (self.A, self.B, self.D))

    @property
    def missing_up_count(self) -> int:
        return sum(value > self.n for value in (self.A, self.B, self.D))

    @property
    def best_hidden_value(self) -> int:
        return min(self.A, self.B, self.D)

    @property
    def best_hidden_mode(self) -> str:
        values = {"A": self.A, "B": self.B, "D": self.D}
        minimum = min(values.values())
        return next(mode for mode in HIDDEN_MODE_ORDER if values[mode] == minimum)

    @property
    def delta_reset_log2(self) -> float:
        return math.log2(self.C) - math.log2(self.A)

    @property
    def delta_hidden_log2(self) -> float:
        return math.log2(self.C) - math.log2(self.best_hidden_value)

    @property
    def height_g(self) -> float:
        return math.log2(3.0 + 1.0 / self.n) - self.a31

    @property
    def epsilon(self) -> float:
        return self.a31 - math.log2(3.0)

    @property
    def eta(self) -> float:
        return math.log2(1.0 + 1.0 / (3.0 * self.n))


def state_features(n: int) -> StateFeatures:
    if n <= 0 or n % 2 == 0:
        raise ValueError("state must be a positive odd integer")
    x11 = n + 1
    x13 = n + 3
    x31 = 3 * n + 1
    x33 = 3 * n + 3
    a11 = v2(x11)
    a13 = v2(x13)
    a31 = v2(x31)
    a33 = v2(x33)
    return StateFeatures(
        n=n,
        A=x11 >> a11,
        B=x13 >> a13,
        C=x31 >> a31,
        D=x33 >> a33,
        a11=a11,
        a13=a13,
        a31=a31,
        a33=a33,
    )


def collatz_next(n: int) -> int:
    x = 3 * n + 1
    return x >> v2(x)


def exact_sanity_failures(n: int) -> list[str]:
    """Return failed exact assertions for one odd n; n=1,3 are boundaries."""
    f = state_features(n)
    failures: list[str] = []
    for mode, value in zip(MODE_ORDER, (f.A, f.B, f.C, f.D)):
        if value <= 0 or value % 2 == 0:
            failures.append(f"{mode}_NOT_POSITIVE_ODD")

    if n > 3:
        if sorted((f.a31, f.a33))[0] != 1 or max(f.a31, f.a33) < 2:
            failures.append("C_D_VALUATION_COMPLEMENTARITY")
        if not f.A < n:
            failures.append("A_NOT_FOLD")
        if not f.B < n:
            failures.append("B_NOT_FOLD")
        directions = [direction(value, n) for value in (f.A, f.B, f.C, f.D)]
        if directions.count("UP") != 1 or directions.count("FOLD") != 3:
            failures.append("NOT_EXACTLY_1_UP_3_FOLD")
        if f.C % 3 == 0:
            failures.append("C_ON_MULT3_SHEET")
        if f.D % 3 != 0:
            failures.append("D_OFF_MULT3_SHEET")
        if (f.actual_direction == "UP") != (n % 4 == 3):
            failures.append("C_UP_MOD4")
        if (f.actual_direction == "FOLD") != (n % 4 == 1):
            failures.append("C_FOLD_MOD4")

    residue = n % 8
    if residue == 1 and f.a31 != 2:
        failures.append("MOD8_1_DEPTH")
    if residue == 3 and f.a31 != 1:
        failures.append("MOD8_3_DEPTH")
    if residue == 5 and f.a31 < 3:
        failures.append("MOD8_5_DEPTH")
    if residue == 7 and (f.a31 != 1 or f.C % 4 != 3):
        failures.append("MOD8_7_DEPTH_OR_SUCCESSOR")
    return failures


def trajectory_states(
    start: int,
    step_cap: int,
    next_cache: dict[int, int] | None = None,
) -> tuple[list[int], str, int]:
    """Return nonterminal states, status, and terminal/current state.

    The terminal state 1 is not included in the returned state list.  Reaching
    the cap is right-censored and never labelled divergent.
    """
    if start <= 0 or start % 2 == 0:
        raise ValueError("start must be a positive odd integer")
    cache = next_cache if next_cache is not None else {}
    states: list[int] = []
    current = start
    seen: dict[int, int] = {}
    for _ in range(step_cap):
        if current == 1:
            return states, "REACHED_1", current
        if current in seen:
            return states, "REPEATED_STATE", current
        seen[current] = len(states)
        states.append(current)
        nxt = cache.get(current)
        if nxt is None:
            nxt = collatz_next(current)
            cache[current] = nxt
        current = nxt
    if current == 1:
        return states, "REACHED_1", current
    return states, "UNRESOLVED_WITHIN_CAP", current


def maximal_runs(values: Sequence[int], predicate) -> Iterator[tuple[int, int]]:
    start: int | None = None
    for index, value in enumerate(values):
        if predicate(value):
            if start is None:
                start = index
        elif start is not None:
            yield start, index - 1
            start = None
    if start is not None:
        yield start, len(values) - 1


def run_max_length(values: Sequence[int], predicate) -> int:
    return max((end - start + 1 for start, end in maximal_runs(values, predicate)), default=0)


def wait_to_next(values: Sequence[int], index: int, threshold: int) -> int | None:
    for future in range(index + 1, len(values)):
        if values[future] >= threshold:
            return future - index
    return None


def rolling_sum(values: Sequence[float], width: int, index: int) -> float | None:
    if index < width:
        return None
    return math.fsum(values[index - width : index])


def encode_depth_factor(values: Sequence[int]) -> int | None:
    code = 0
    for value in values:
        if value == 1:
            bit = 0
        elif value == 2:
            bit = 1
        else:
            return None
        code = (code << 1) | bit
    return code


def factor_sets_from_binary(binary: Sequence[int], max_length: int) -> dict[int, set[int]]:
    """Return rolling-bit factor sets for lengths 1..max_length."""
    result: dict[int, set[int]] = {}
    size = len(binary)
    for length in range(1, max_length + 1):
        if length > size:
            result[length] = set()
            continue
        mask = (1 << length) - 1
        code = 0
        factors: set[int] = set()
        for index, bit in enumerate(binary):
            code = ((code << 1) | bit) & mask
            if index + 1 >= length:
                factors.add(code)
        result[length] = factors
    return result


def longest_factor_match(values: Sequence[int], factor_sets: dict[int, set[int]]) -> int:
    """Longest contiguous {1,2} word present in the supplied factor language."""
    maximum = max(factor_sets, default=0)
    best = 0
    for run_start, run_end in maximal_runs(values, lambda value: value in (1, 2)):
        run = values[run_start : run_end + 1]
        upper = min(len(run), maximum)
        for length in range(upper, best, -1):
            found = False
            mask = (1 << length) - 1
            code = 0
            for index, value in enumerate(run):
                code = ((code << 1) | (value - 1)) & mask
                if index + 1 >= length and code in factor_sets[length]:
                    found = True
                    break
            if found:
                best = length
                break
    return best


def first_critical_break(values: Sequence[int], factor_sets: dict[int, set[int]]) -> str:
    """Classify the first break of the prefix-compatible critical language."""
    code = 0
    length = 0
    maximum = max(factor_sets, default=0)
    for value in values:
        if value >= 3:
            return "DEEP_FOLD"
        if value not in (1, 2):
            return "OUTSIDE_ALPHABET"
        if length >= maximum:
            return "FACTOR_CAP_REACHED"
        code = (code << 1) | (value - 1)
        length += 1
        if code not in factor_sets[length]:
            return "CRITICAL_FORBIDDEN_GRAMMAR"
    return "NO_BREAK_BEFORE_TERMINAL_OR_CAP"


def count_windows(
    values: Sequence[int],
    lengths: Iterable[int],
    factor_sets: dict[int, set[int]],
) -> dict[int, tuple[int, int, int]]:
    """Return total, {1,2}-alphabet, and critical-language window counts."""
    result: dict[int, tuple[int, int, int]] = {}
    for length in lengths:
        total = max(0, len(values) - length + 1)
        alphabet = 0
        critical = 0
        if total:
            mask = (1 << length) - 1
            code = 0
            outside = 0
            for index, value in enumerate(values):
                if value in (1, 2):
                    bit = value - 1
                else:
                    bit = 0
                    outside += 1
                code = ((code << 1) | bit) & mask
                if index >= length:
                    leaving = values[index - length]
                    if leaving not in (1, 2):
                        outside -= 1
                if index + 1 >= length and outside == 0:
                    alphabet += 1
                    if code in factor_sets[length]:
                        critical += 1
        result[length] = (total, alphabet, critical)
    return result


def valuation_label(mu: int, c: int, residue: int, bits: int) -> tuple[str, int | None]:
    modulus = 1 << bits
    value = (mu * residue + c) % modulus
    if value == 0:
        return f">={bits}", None
    depth = v2(value)
    return str(depth), depth


def stable_affine_order(
    residue: int,
    bits: int,
    depths: dict[str, int | None],
) -> str:
    """Exact output order if fixed on the positive residue cylinder."""
    if any(depth is None for depth in depths.values()):
        return "VARIABLE_WITHIN_CYLINDER"
    modes = {
        "A": (1, 1),
        "B": (1, 3),
        "C": (3, 1),
        "D": (3, 3),
    }
    n0 = residue
    modulus = 1 << bits

    def numerator(mode: str, n: int) -> int:
        mu, c = modes[mode]
        return (mu * n + c) >> int(depths[mode])

    for left_index, left in enumerate(MODE_ORDER):
        for right in MODE_ORDER[left_index + 1 :]:
            d_left = int(depths[left])
            d_right = int(depths[right])
            mu_left, c_left = modes[left]
            mu_right, c_right = modes[right]
            common = max(d_left, d_right)
            slope = (mu_left << (common - d_left)) - (mu_right << (common - d_right))
            intercept = (c_left << (common - d_left)) - (c_right << (common - d_right))
            at_start = slope * n0 + intercept
            step = slope * modulus
            if at_start == 0:
                if step != 0:
                    return "VARIABLE_WITHIN_CYLINDER"
            elif at_start > 0 and step < 0:
                crossing = (-at_start + (-step) - 1) // (-step)
                if crossing >= 1:
                    return "VARIABLE_WITHIN_CYLINDER"
            elif at_start < 0 and step > 0:
                crossing = (-at_start + step - 1) // step
                if crossing >= 1:
                    return "VARIABLE_WITHIN_CYLINDER"

    ordered = sorted(MODE_ORDER, key=lambda mode: (numerator(mode, n0), MODE_ORDER.index(mode)))
    groups: list[str] = []
    for mode in ordered:
        value = numerator(mode, n0)
        if groups and value == numerator(groups[-1].split("=")[0], n0):
            groups[-1] += f"={mode}"
        else:
            groups.append(mode)
    return "<".join(groups)


def residue_signature_row(bits: int, residue: int) -> dict[str, object]:
    specs = {"A": (1, 1), "B": (1, 3), "C": (3, 1), "D": (3, 3)}
    labels: dict[str, str] = {}
    depths: dict[str, int | None] = {}
    for mode, (mu, c) in specs.items():
        label, depth = valuation_label(mu, c, residue, bits)
        labels[mode] = label
        depths[mode] = depth

    a31 = depths["C"]
    actual_direction = "FOLD" if a31 is None or a31 >= 2 else "UP"
    ordering = stable_affine_order(residue, bits, depths)
    if ordering == "VARIABLE_WITHIN_CYLINDER":
        best_hidden = "VARIABLE_WITHIN_CYLINDER"
    else:
        first_group = ordering.split("<", 1)[0].split("=")
        hidden = [mode for mode in first_group if mode in HIDDEN_MODE_ORDER]
        if hidden:
            best_hidden = "=".join(hidden)
        else:
            # The global minimum can be C; choose the first hidden group.
            best_hidden = next(
                group for group in ordering.split("<") if any(m in HIDDEN_MODE_ORDER for m in group.split("="))
            )

    return {
        "modulus": 1 << bits,
        "bits": bits,
        "odd_residue": residue,
        "a11": labels["A"],
        "a13": labels["B"],
        "a31": labels["C"],
        "a33": labels["D"],
        "coarse_signature": f"({labels['A']},{labels['B']},{labels['C']},{labels['D']})",
        "output_ordering": ordering,
        "actual_C_direction": actual_direction,
        "best_hidden_mode": best_hidden,
        "missing_down_count": 3 if actual_direction == "UP" else 2,
        "missing_up_count": 0 if actual_direction == "UP" else 1,
        "D_sheet_switching_ability": "YES_TO_MULT3",
    }
