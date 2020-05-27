import unittest
from unittest.mock import patch

from .solution_456A import Solution456A


class TestSolution456A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution456A()

    def test_456A_acceptance_1(self):
        mock_input = ["2", "1 2", "2 1"]
        expected = "Happy Alex"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
