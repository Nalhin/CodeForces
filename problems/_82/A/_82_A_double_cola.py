"""
    Submission - https://codeforces.com/contest/82/submission/134343313
"""

friends = ["Sheldon", "Leonard", "Penny", "Rajesh", "Howard"]


def main() -> None:
    n = int(input()) - 1

    curr_sum = 0
    curr_amount = 5

    while curr_sum + curr_amount <= n:
        curr_sum += curr_amount
        curr_amount *= 2

    remaining = n - curr_sum
    friend_idx = remaining * 5 // curr_amount

    print(friends[friend_idx])


if __name__ == '__main__':
    main()
