class Solution281A:
    def __init__(self):
        self.result = ""

    def parse_input(self):
        self.result = input()

    def solve(self):
        self.result = self.result[0].upper() + self.result[1:]

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution281A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
