"""
    Submission - https://codeforces.com/contest/112/submission/134247290
"""


def main():
    str1 = input().lower()
    str2 = input().lower()

    if str1 > str2:
        print(1)
    elif str1 < str2:
        print(-1)
    else:
        print(0)


if __name__ == '__main__':
    main()
