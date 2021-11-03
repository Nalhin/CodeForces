"""
    Submission - https://codeforces.com/contest/519/submission/134248331
"""
from collections import Counter


def main():
    _ = input()

    first_errors = [int(e) for e in input().split()]
    second_errors = [int(e) for e in input().split()]
    third_errors = [int(e) for e in input().split()]

    print(next((Counter(first_errors) - Counter(second_errors)).elements()))
    print(next((Counter(second_errors) - Counter(third_errors)).elements()))


if __name__ == '__main__':
    main()
