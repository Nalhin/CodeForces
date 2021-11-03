"""
    Submission - https://codeforces.cc/contest/71/submission/134157595
"""


def main() -> None:
    n = int(input())
    for _ in range(n):
        word = input()
        print(word if (len(word) <= 10) else word[0] + str(len(word) - 2) + word[-1])


if __name__ == '__main__':
    main()
