class Solution112A:
    def __init__(self):
        self.words = []
        self.result = ""

    def parse_input(self):
        self.words.append(input().lower())
        self.words.append(input().lower())

    def solve(self):
        first, second = self.words

        if first == second:
            self.result = "0"
        elif first < second:
            self.result = "-1"
        else:
            self.result = "1"

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution112A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
