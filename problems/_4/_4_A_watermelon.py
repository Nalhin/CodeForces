"""
    Submission - https://codeforces.com/contest/4/submission/134157545
"""


def main():
    weight = int(input())
    print("YES" if (weight > 3 and weight % 2 == 0) else "NO")


if __name__ == '__main__':
    main()
