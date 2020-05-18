import unittest
from unittest.mock import patch

from .solution_617A import Solution617A


class TestSolution617A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution617A()

    def test_617A_acceptance_1(self):
        mock_input = ["5"]
        expected = "1"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)

    def test_617A_acceptance_2(self):
        mock_input = ["12"]
        expected = "3"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
