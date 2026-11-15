import unittest
from pathlib import Path
from tempfile import TemporaryDirectory

import numpy as np

from analyze import build_grid, extract_drums, to_pos


class GridTests(unittest.TestCase):
    def test_phase_zero_keeps_the_opening_bar_and_pickup_notes(self):
        grid, boundaries = build_grid(123.62, 0.032, 392.67, 0)
        self.assertAlmostEqual(boundaries[0], 0.032)
        self.assertEqual(to_pos(0.546, grid)[:2], (1, 5))
        self.assertEqual(to_pos(15.56, grid)[:2], (9, 1))
        self.assertEqual(grid["complete_bars"], 202)
        self.assertEqual(grid["n_bars"], 203)

    def test_partial_tail_is_clipped_without_a_phantom_bar_at_an_exact_end(self):
        exact, boundaries = build_grid(120, 0.03, 4.03, 0)
        self.assertEqual(exact["n_bars"], 2)
        self.assertEqual(exact["partial_final_bar_s"], 0)
        np.testing.assert_allclose(boundaries, [0.03, 2.03, 4.03])
        partial, boundaries = build_grid(120, 0.03, 4.5, 0)
        self.assertEqual(partial["complete_bars"], 2)
        self.assertEqual(partial["n_bars"], 3)
        self.assertAlmostEqual(partial["partial_final_bar_s"], 0.47)
        self.assertEqual(boundaries[-1], 4.5)

    def test_grid_rejects_nonfinite_or_out_of_audio_downbeats(self):
        for arguments in [(0, 0, 4, 0), (120, float("nan"), 4, 0), (120, 0, 0.4, 3)]:
            with self.subTest(arguments=arguments), self.assertRaises(ValueError):
                build_grid(*arguments)

    def test_missing_drum_lane_fails_instead_of_saving_an_incomplete_success(self):
        grid, _ = build_grid(120, 0, 4, 0)
        with TemporaryDirectory() as directory, self.assertRaises(FileNotFoundError):
            extract_drums(Path(directory), Path(directory), grid, -15)


if __name__ == "__main__":
    unittest.main()
