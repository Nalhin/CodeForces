"""
    Submission - https://codeforces.com/contest/118/submission/134227670
"""

VOWELS = {'a', 'o', 'y', 'e', 'u', 'i'}


def main() -> None:
    word = input()
    parsed_letters = [f".{letter.lower()}" for letter in word if letter.lower() not in VOWELS]
    print("".join(parsed_letters))


if __name__ == '__main__':
    main()
