class Solution1117B:
    def __init__(self):
        self.m = 0
        self.k = 0
        self.happiness_values = []
        self.result = 0

    def parse_input(self):
        _, self.m, self.k = [int(i) for i in input().split(" ")]
        self.happiness_values = [int(i) for i in input().split(" ")]

    def solve(self):
        largest, second_largest = self.happiness_values.sort(reverse=True)[:2]

        second_largest_use_count = self.m // (self.k + 1)
        largest_use_count = self.m - second_largest_use_count

        self.result = (
            largest_use_count * largest
            + second_largest_use_count * second_largest
        )

    def get_result(self):
        return str(self.result)


if __name__ == "__main__":
    solution = Solution1117B()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
