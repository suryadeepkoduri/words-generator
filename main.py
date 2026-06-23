import secrets
import sys

from wordfreq import top_n_list


def main():
    args = sys.argv[1:]
    common_words = top_n_list("en", 10000)
    filtered = tuple(w for w in common_words if 3 <= len(w) <= 7 and w.isalpha())
    length = 3

    if len(args) > 0:
        length = int(args[0])

    words = []
    for _ in range(length):
        words.append(secrets.choice(filtered))
    print(*words, sep="-")


if __name__ == "__main__":
    main()
