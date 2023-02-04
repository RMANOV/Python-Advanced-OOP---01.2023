# Test Code
import unittest
from samplerange import rangeDay


class RangeDayTest(unittest.TestCase):
    def setUp(self):
        self.field = [
            [".", "x", ".", "x", "."],
            [".", ".", "A", ".", "x"],
            [".", "x", ".", "x", "."],
            ["x", ".", "x", ".", "x"],
            ["x", "x", ".", "x", ".0"],
        ]

    def test_not_all_targets_hit(self):
        output = "Training not completed! 2 targets left".split(" ")

        self.assertEqual(rangeDay(self.field, 15), output)

    def test_all_targets_hit(self):
        output = "Training completed! All 7 targets hit".split(" ")

        self.assertEqual(rangeDay(self.field, 20), output)
