class Solution456A:
    def __init__(self):
        self.result = False
        self.sets = []

    def parse_input(self):
        num_of_sets = int(input())
        for _ in range(num_of_sets):
            self.sets.append([int(i) for i in input().split(" ")])

    def solve(self):
        by_price = sorted(self.sets, key=lambda el: el[0])
        by_quality = sorted(self.sets, key=lambda el: el[1])

        for a, b in zip(by_price, by_quality):
            if a[0] > b[0]:
                self.result = True

    def get_result(self):
        return "Happy Alex" if self.result else "Poor Alex"


if __name__ == "__main__":
    solution = Solution456A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
