"""
    Submission - https://codeforces.com/contest/75/submission/134351902
"""
from collections import defaultdict

POINTS_PER_ACTION = {
    'posted': 15,
    'commented': 10,
    'likes': 5
}


def main() -> None:
    me = input()
    n = int(input())

    scores = defaultdict(int)

    for _ in range(n):
        post = input().split()
        author = post[0]
        action = post[1]
        target = post[-2][:-2]

        if author == me:
            scores[target] += POINTS_PER_ACTION[action]
        else:
            scores[author] += 0

        if target == me:
            scores[author] += POINTS_PER_ACTION[action]
        else:
            scores[target] += 0

    if me in scores:
        scores.pop(me)
    for name, _ in sorted(scores.items(), key=lambda x: (-x[1], x[0])):
        print(name)


if __name__ == '__main__':
    main()
