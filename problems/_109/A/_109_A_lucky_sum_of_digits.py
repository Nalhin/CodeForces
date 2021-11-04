"""
    Submission - https://codeforces.com/contest/109/submission/134344455
"""


def main() -> None:
    n = int(input())

    curr = 0

    while n % 7 != 0:
        curr *= 10
        curr += 4
        n -= 4

    if n < 0:
        print(-1)
    else:
        print((str(curr) if curr != 0 else "") + "7" * (n // 7))


if __name__ == '__main__':
    main()
