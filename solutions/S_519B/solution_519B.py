from collections import Counter


class Solution519B:
    def __init__(self):
        self.result = ""
        self.first_set = []
        self.second_set = []
        self.last_set = []

    def parse_input(self):
        int(input())
        self.first_set = [int(i) for i in input().split(" ")]
        self.second_set = [int(i) for i in input().split(" ")]
        self.last_set = [int(i) for i in input().split(" ")]

    def solve(self):
        c_first = Counter(self.first_set)
        c_second = Counter(self.second_set)
        c_last = Counter(self.last_set)

        self.result += f"{list((c_first - c_second).keys())[0]}\n"
        self.result += f"{list((c_second - c_last).keys())[0]}"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution519B()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
