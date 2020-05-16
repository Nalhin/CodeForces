import math


class Solution617A:
    def __init__(self):
        self.length = 0
        self.result = 0

    def parse_input(self):
        self.length = int(input())

    def solve(self):
        self.result = math.ceil(self.length / 5)

    def get_result(self):
        return str(self.result)


if __name__ == "__main__":
    solution = Solution617A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
