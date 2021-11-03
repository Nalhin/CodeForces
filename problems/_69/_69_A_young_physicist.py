"""
    Submission - https://codeforces.com/contest/69/submission/134249945
"""


def main():
    n = int(input())

    sums = [0] * 3

    for _ in range(n):
        for i, val in enumerate([int(x) for x in input().split()]):
            sums[i] += val

    print("YES" if all(single_sum == 0 for single_sum in sums) else "NO")


if __name__ == '__main__':
    main()
