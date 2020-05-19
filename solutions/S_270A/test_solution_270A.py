import unittest
from unittest.mock import patch

from .solution_270A import Solution270A


class TestSolution270A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution270A()

    def test_270A_acceptance_1(self):
        mock_input = ["3", "30", "60", "90"]
        expected = "NO\nYES\nYES"

        with patch("builtins.input", side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
