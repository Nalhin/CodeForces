"""
    Submission - https://codeforces.com/contest/282/submission/134257082
"""


def main() -> None:
    n = int(input())

    words = [input() for _ in range(n)]
    print(sum((1 if '+' in word else -1 for word in words)))


if __name__ == '__main__':
    main()
