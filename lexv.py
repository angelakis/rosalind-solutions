import itertools


if __name__ == "__main__":
    with open("inputfiles/rosalind_lexv.txt") as f:
        symbols = f.readline().strip().split()
        length = int(f.readline().strip())
    symbols = ["@"] + symbols
    words = ["".join(w) for w in itertools.product(symbols, repeat=length)]
    words = [
        w.replace("@", "") for w in words[1:]  # remove @@@
        if w.startswith(w.replace("@", ""))
    ]
    words = list(dict.fromkeys(words))
    print("\n".join(words))
