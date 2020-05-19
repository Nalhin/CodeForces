import unittest
from unittest.mock import patch

from .solution_82A import Solution82A


class TestSolution82A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution82A()

    def test_82A_acceptance_1(self):
        mock_input = ['1']
        expected = "Sheldon"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_82A_acceptance_2(self):
        mock_input = ['6']
        expected = "Sheldon"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_82A_acceptance_3(self):
        mock_input = ['1802']
        expected = "Penny"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
