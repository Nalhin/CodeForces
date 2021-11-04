"""
    Submission - https://codeforces.com/contest/270/submission/134308836
"""


def main() -> None:
    n = int(input())

    for _ in range(n):
        t = int(input())

        n = 360 / (180 - t)
        print("YES" if n.is_integer() else "NO")


if __name__ == '__main__':
    main()
