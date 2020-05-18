import unittest
from unittest.mock import patch

from .solution_281A import Solution281A


class TestSolution281A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution281A()

    def test_281A_acceptance_1(self):
        mock_input = ["ApPLe"]
        expected = "ApPLe"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_281A_acceptance_2(self):
        mock_input = ["konjac"]
        expected = "Konjac"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
