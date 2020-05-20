import unittest
from unittest.mock import patch

from .solution_519B import Solution519B


class TestSolution519B(unittest.TestCase):
    def setUp(self):
        self.solution = Solution519B()

    def test_519B_acceptance_1(self):
        mock_input = ["5", "1 5 8 123 7", "123 7 5 1", "5 1 7"]
        expected = "8\n123"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_519B_acceptance_2(self):
        mock_input = ["6", "1 4 3 3 5 7", "3 7 5 4 3", "4 3 7 5"]
        expected = "1\n3"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
