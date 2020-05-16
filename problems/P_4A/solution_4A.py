class Solution4A:
    def __init__(self):
        self.w = None
        self.result = ''

    def parse_input(self):
        self.w = int(input())

    def solve(self):
        self.result = "NO" if self.w % 2 == 1 else "YES"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution4A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
