import unittest
from unittest.mock import patch

from .solution_158B import Solution158B


class TestSolution158B(unittest.TestCase):
    def setUp(self):
        self.solution = Solution158B()

    def test_158B_acceptance_1(self):
        mock_input = ["5", "1 2 4 3 3"]
        expected = "4"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_158B_acceptance_2(self):
        mock_input = ["8", "2 3 4 4 2 1 3 1"]
        expected = "5"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
