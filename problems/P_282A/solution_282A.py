class Solution282A:
    def __init__(self):
        self.operations = []
        self.result = 0

    def parse_input(self):
        numbers = int(input())
        for _ in range(numbers):
            self.operations.append(input())

    def solve(self):
        for operation in self.operations:
            if "++" in operation:
                self.result += 1
            else:
                self.result -= 1

    def get_result(self):
        return str(self.result)


if __name__ == "__main__":
    solution = Solution282A()
    solution.parse_input()
    solution.solve()
    print(solution.get_result())
