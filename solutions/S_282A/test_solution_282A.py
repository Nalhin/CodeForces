import unittest
from unittest.mock import patch

from .solution_282A import Solution282A


class TestSolution282A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution282A()

    def test_282A_acceptance_1(self):
        mock_input = ["1", "++X"]
        expected = "1"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)

    def test_282A_acceptance_2(self):
        mock_input = ["2", "X++", "--X"]
        expected = "0"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)


if __name__ == "__main__":
    unittest.main()
