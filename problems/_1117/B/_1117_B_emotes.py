"""
    Submission - https://codeforces.com/contest/1117/submission/134259180
"""
from typing import List, Tuple


def main() -> None:
    _, m, k = (int(num) for num in input().split())
    happiness = [int(num) for num in input().split()]

    max_val, second_max_val = find_max_and_second_max(happiness)

    second_usages = m // (k + 1)
    first_usages = m - second_usages
    result = max_val * first_usages + second_max_val * second_usages
    print(result)


def find_max_and_second_max(nums: List[int]) -> Tuple[int, int]:
    max_idx = 0 if nums[0] >= nums[1] else 1
    second_max_idx = 1 if nums[0] >= nums[1] else 0

    for i in range(2, len(nums)):
        if nums[i] >= nums[max_idx]:
            second_max_idx = max_idx
            max_idx = i
        else:
            if nums[i] > nums[second_max_idx]:
                second_max_idx = i

    return nums[max_idx], nums[second_max_idx]


if __name__ == '__main__':
    main()
