import unittest
from unittest.mock import patch

from .solution_1117B import Solution1117B


class TestSolution1117B(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1117B()

    def test_1117B_acceptance_1(self):
        mock_input = ["6 9 2", "1 3 3 7 4 2"]
        expected = "54"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_1117B_acceptance_2(self):
        mock_input = ["3 1000000000 1", "1000000000 987654321 1000000000"]
        expected = "1000000000000000000"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
