import unittest
from unittest.mock import patch

from .solution_4A import Solution4A


class TestSolution4A(unittest.TestCase):
    def setUp(self):
        self.solution = Solution4A()

    def test_4A_acceptance_1(self):
        mock_input = ['8']
        expected = 'YES'

        with patch('builtins.input', side_effect=mock_input):
            self.solution.parse_input()
            self.solution.solve()
            result = self.solution.get_result()

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
