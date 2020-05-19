import unittest
from unittest.mock import patch

from .solution_69A import Solution69A


class TestSolution69A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution69A()

    def test_69A_acceptance_1(self):
        mock_input = ['3', '4 1 7', '-2 4 -1', '1 -5 -3']
        expected = "NO"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_69A_acceptance_2(self):
        mock_input = ['3', '3 -1 7', '-5 2 -4', '2 -1 -3']
        expected = "YES"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
