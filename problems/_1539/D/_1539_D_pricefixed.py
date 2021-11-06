"""
    Submission - https://codeforces.com/contest/1539/submission/134484197
"""
from operator import itemgetter


def main() -> None:
    n = int(input())

    products = [[int(i) for i in input().split()] for _ in range(n)]
    products.sort(key=itemgetter(1))

    left = 0
    right = len(products) - 1
    total_bought = 0
    total_cost = 0

    while left <= right:
        if products[left][1] <= total_bought:
            total_cost += products[left][0]
            total_bought += products[left][0]
            left += 1
        else:
            to_buy = min(products[left][1] - total_bought, products[right][0])
            total_cost += to_buy * 2
            total_bought += to_buy
            products[right][0] -= to_buy
            if products[right][0] == 0:
                right -= 1

    print(total_cost)


if __name__ == '__main__':
    main()
