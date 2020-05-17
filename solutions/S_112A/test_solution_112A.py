import unittest
from unittest.mock import patch

from .solution_112A import Solution112A


class TestSolution112A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution112A()

    def test_112A_acceptance_1(self):
        mock_input = ['aaaa', 'aaaA']
        expected = '0'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)

    def test_112A_acceptance_2(self):
        mock_input = ['abs', 'Abz']
        expected = '-1'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)

    def test_112A_acceptance_3(self):
        mock_input = ['abcdefg', 'AbCdEfF']
        expected = '1'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
