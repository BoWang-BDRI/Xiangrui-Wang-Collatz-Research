from __future__ import annotations

import json
import math
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
sys.path.insert(0, str(ROOT))

from control_deficit_core import (  # noqa: E402
    count_windows,
    exact_sanity_failures,
    factor_sets_from_binary,
    residue_signature_row,
    state_features,
    trajectory_states,
)
from run_atlas import generate_sturmian, summary_for_orbit  # noqa: E402


class ExactCoreTests(unittest.TestCase):
    def test_known_four_mode_nodes(self) -> None:
        five = state_features(5)
        self.assertEqual((five.A, five.B, five.C, five.D), (3, 1, 1, 9))
        self.assertEqual((five.a11, five.a13, five.a31, five.a33), (1, 3, 4, 1))
        seven = state_features(7)
        self.assertEqual((seven.A, seven.B, seven.C, seven.D), (1, 5, 11, 3))
        self.assertEqual((seven.a11, seven.a13, seven.a31, seven.a33), (3, 1, 1, 3))

    def test_exact_sanity_through_9999(self) -> None:
        for n in range(1, 10_000, 2):
            self.assertEqual(exact_sanity_failures(n), [], n)

    def test_height_cocycle_identity(self) -> None:
        for n in range(1, 1000, 2):
            feature = state_features(n)
            self.assertAlmostEqual(feature.height_g, -feature.epsilon + feature.eta, places=13)
            self.assertAlmostEqual(feature.height_g, math.log2(feature.C / n), places=13)

    def test_named_27_reaches_one_and_telescopes(self) -> None:
        states, status, terminal = trajectory_states(27, 1000, {})
        self.assertEqual(status, "REACHED_1")
        self.assertEqual(terminal, 1)
        self.assertEqual(states[:5], [27, 41, 31, 47, 71])
        g_sum = math.fsum(state_features(n).height_g for n in states)
        self.assertAlmostEqual(g_sum, math.log2(1 / 27), places=12)

    def test_boundary_nodes_are_explicit(self) -> None:
        one = state_features(1)
        three = state_features(3)
        self.assertEqual((one.A, one.B, one.C, one.D), (1, 1, 1, 3))
        self.assertEqual((three.A, three.B, three.C, three.D), (1, 3, 5, 3))
        self.assertEqual(exact_sanity_failures(1), [])
        self.assertEqual(exact_sanity_failures(3), [])

    def test_sturmian_candidate_and_complexity(self) -> None:
        binary, metadata = generate_sturmian(10_000)
        self.assertEqual(metadata["candidate_formula_mismatches"], 0)
        self.assertTrue(metadata["alphabet_subset_1_2"])
        self.assertTrue(metadata["no_consecutive_a1"])
        factors = factor_sets_from_binary(binary, 64)
        self.assertEqual({length: len(words) for length, words in factors.items()}, {length: length + 1 for length in range(1, 65)})

    def test_rolling_window_counter(self) -> None:
        binary, _ = generate_sturmian(1000)
        factors = factor_sets_from_binary(binary, 16)
        depths = [bit + 1 for bit in binary[:100]] + [3] + [bit + 1 for bit in binary[100:200]]
        counts = count_windows(depths, (8, 16), factors)
        self.assertGreater(counts[8][0], counts[8][1])
        self.assertEqual(counts[8][1], counts[8][2])

    def test_residue_atlas_uses_lower_bound_labels(self) -> None:
        row = residue_signature_row(3, 5)
        self.assertEqual(row["a31"], ">=3")
        self.assertEqual(row["actual_C_direction"], "FOLD")
        row = residue_signature_row(3, 7)
        self.assertEqual(row["a31"], "1")
        self.assertEqual(row["actual_C_direction"], "UP")

    def test_config_has_required_full_limits(self) -> None:
        config = json.loads((ROOT / "config.json").read_text(encoding="utf-8"))
        self.assertEqual(config["tier_b_max_inclusive"], 1_000_000)
        self.assertEqual(config["tier_c_count"], 50_000)
        self.assertEqual(config["tier_c_step_cap"], 100_000)
        self.assertEqual(config["sturmian_odd_return_symbols"], 1_000_000)
        self.assertEqual(config["public_seed"], 20260826)


if __name__ == "__main__":
    unittest.main()
