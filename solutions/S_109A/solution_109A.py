class Solution109A:
    def __init__(self):
        self.result = ""
        self.n = 0

    def parse_input(self):
        self.n = int(input())

    def solve(self):
        while self.n % 7 != 0:
            if self.n < 0:
                self.result = "-1"
                return
            self.n -= 4
            self.result += "4"

        sevens = self.n // 7
        self.result += "7" * sevens

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution109A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
