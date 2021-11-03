"""
    Submission - https://codeforces.com/contest/231/submission/134237568
"""


def main():
    n = int(input())

    result = 0

    for _ in range(n):
        friends = sum([int(num) for num in input().split()])
        if friends >= 2:
            result += 1

    print(result)


if __name__ == '__main__':
    main()
