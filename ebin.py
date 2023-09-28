from decimal import Decimal

if __name__ == "__main__":
    with open("rosalind_ebin.txt") as f:
        n = int(f.readline().strip())
        freqs = map(Decimal, f.readline().strip().split())
    print(" ".join([str(n * f) for f in freqs]))
