"""
    Submission - https://codeforces.com/contest/1/submission/134249306
"""
from math import ceil


def main() -> None:
    n, m, a = [int(i) for i in input().split()]

    print(ceil(n / a) * ceil(m / a))


if __name__ == '__main__':
    main()
