"""
    Submission - https://codeforces.com/contest/158/submission/134257976
"""
from typing import List


def main() -> None:
    n, k = (int(i) for i in input().split())
    scores = [int(i) for i in input().split()]

    print(solve(k, scores) + 1)


def solve(k: int, scores: List[int]) -> int:
    if scores[k - 1] == 0:
        return binary_search_last_equal_or_greater(scores, 1, 0, k)
    else:
        return binary_search_last_equal_or_greater(scores, scores[k - 1], 0, len(scores) - 1)


def binary_search_last_equal_or_greater(scores: List[int], value: int, left: int, right: int) -> int:
    result = -1

    while left <= right:
        mid = left + (right - left) // 2
        if scores[mid] >= value:
            left = mid + 1
            result = mid
        else:
            right = mid - 1

    return result


if __name__ == '__main__':
    main()
