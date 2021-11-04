"""
    Submission - https://codeforces.com/contest/158/submission/134306772
"""
from collections import defaultdict

MAX = 4


def main() -> None:
    _ = input()

    groups = [int(i) for i in input().split()]
    counts = defaultdict(int)
    for num in groups:
        counts[num] += 1

    left = 1
    right = MAX

    result = 0
    curr_sum = 0

    while left <= right:
        while left <= right and counts[left] == 0:
            left += 1
        while left <= right and counts[right] == 0:
            right -= 1

        if left <= right:
            if right + curr_sum <= MAX:
                curr_sum += right
                counts[right] -= 1
            else:
                if left + curr_sum <= MAX:
                    curr_sum += left
                    counts[left] -= 1
                else:
                    result += 1
                    curr_sum = 0

    print(result + 1 if curr_sum != 0 else 0)


if __name__ == '__main__':
    main()
