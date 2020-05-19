class Solution270A:
    def __init__(self):
        self.result = []
        self.alpha = 0
        self.cases = []

    def parse_input(self):
        t = int(input())
        for _ in range(t):
            self.cases.append(int(input()))

    def solve(self):
        for angle in self.cases:
            n = 360 / (180 - angle)
            if n.is_integer():
                self.result.append("YES")
            else:
                self.result.append("NO")

    def get_result(self):
        return "\n".join(self.result)


if __name__ == "__main__":
    solution = Solution270A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
