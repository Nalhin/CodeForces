"""
    Submission - https://codeforces.com/contest/750/submission/134256594
"""

TIME_TILL_MIDNIGHT = 240


def main() -> None:
    n, k = [int(i) for i in input().split()]

    print(find_time(n, TIME_TILL_MIDNIGHT - k))


def find_time(n: int, time: int) -> int:
    for i in range(n):
        next_task = 5 * (i + 1)
        if next_task <= time:
            time -= next_task
        else:
            return i

    return n


if __name__ == '__main__':
    main()
