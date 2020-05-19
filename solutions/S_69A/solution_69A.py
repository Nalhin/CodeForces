class Solution69A:
    def __init__(self):
        self.result = ""
        self.forces = [0, 0, 0]

    def parse_input(self):
        n = int(input())
        for _ in range(n):
            for i, num in enumerate(input().split(" ")):
                self.forces[i] += int(num)

    def solve(self):
        all_match = all(v == 0 for v in self.forces)
        self.result = "YES" if all_match else "NO"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution69A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
