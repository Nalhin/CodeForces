TAXI_CAPACITY = 4


class Solution158B:
    def __init__(self):
        self.result = 0
        self.n = 0
        self.groups = []

    def parse_input(self):
        self.n = int(input())
        self.groups = [int(i) for i in input().split(" ")]

    def solve(self):
        start_i = 0
        end_i = self.n - 1
        self.groups.sort(reverse=True)

        while start_i <= end_i:
            curr_cap = self.groups[start_i]
            while (
                curr_cap + self.groups[end_i] <= TAXI_CAPACITY
                and start_i <= end_i
            ):
                curr_cap += self.groups[end_i]
                end_i -= 1

            start_i += 1
            self.result += 1

    def get_result(self):
        return str(self.result)


if __name__ == "__main__":
    solution = Solution158B()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
