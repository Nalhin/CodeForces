class Solution750A:
    def __init__(self):
        self.result = ""
        self.k = 0
        self.n = 0
        self.result = 0

    def parse_input(self):
        self.n, self.k = [int(i) for i in input().split(" ")]

    def solve(self):
        total_time = 240
        time_per_exercise = 5
        remaining_time = total_time - self.k

        for i in range(1, self.n + 1):
            remaining_time -= time_per_exercise * i
            if remaining_time < 0:
                break

            self.result += 1

    def get_result(self):
        return str(self.result)


if __name__ == "__main__":
    solution = Solution750A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
