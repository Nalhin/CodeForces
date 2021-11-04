"""
    Submission - https://codeforces.com/contest/456/submission/134350706
"""
from operator import itemgetter


def main() -> None:
    n = int(input())

    pairs = []
    for _ in range(n):
        pairs.append([int(i) for i in input().split()])

    print("Poor Alex" if sorted(pairs, key=itemgetter(0)) == sorted(pairs, key=itemgetter(1)) else "Happy Alex")


if __name__ == '__main__':
    main()
