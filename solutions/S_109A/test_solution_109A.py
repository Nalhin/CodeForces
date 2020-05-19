import unittest
from unittest.mock import patch

from .solution_109A import Solution109A


class TestSolution109A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution109A()

    def test_109A_acceptance_1(self):
        mock_input = ['11']
        expected = "47"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_109A_acceptance_2(self):
        mock_input = ['10']
        expected = "-1"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
