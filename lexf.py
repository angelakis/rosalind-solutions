import itertools


if __name__ == "__main__":
    with open("inputfiles/rosalind_lexf.txt") as f:
        symbols = f.readline().strip().split()
        length = int(f.readline().strip())
    print("\n".join("".join(str) for str in itertools.product(symbols, repeat=length)))
