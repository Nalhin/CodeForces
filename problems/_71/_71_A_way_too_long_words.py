"""
    Submission -
"""


def main():
    n = int(input())
    solve()
    for _ in range(n - 1):
        print()
        solve()


def solve():
    word = input()
    print(word if (len(word) <= 10) else word[0] + str(len(word) - 2) + word[-1], end="")


if __name__ == '__main__':
    main()
