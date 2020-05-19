import math

FRIENDS = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


class Solution82A:
    def __init__(self):
        self.result = ""
        self.n = 0

    def parse_input(self):
        self.n = int(input())

    def solve(self):
        self.result = FRIENDS[self.get_friend_position(self.n - 1)]

    @classmethod
    def get_friend_position(cls, n, base=len(FRIENDS)):
        if n < base:
            return math.floor(n * len(FRIENDS) / base)
        return cls.get_friend_position(n - base, 2 * base)

    def get_result(self):
        return self.result


if __name__ == "__main__":
    solution = Solution82A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
