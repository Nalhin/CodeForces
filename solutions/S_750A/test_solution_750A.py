import unittest
from unittest.mock import patch

from .solution_750A import Solution750A


class TestSolution750A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution750A()

    def test_750A_acceptance_1(self):
        mock_input = ['3 222']
        expected = '2'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)

    def test_750A_acceptance_2(self):
        mock_input = ['4 190']
        expected = '4'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)

    def test_750A_acceptance_3(self):
        mock_input = ['7 1']
        expected = '7'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
