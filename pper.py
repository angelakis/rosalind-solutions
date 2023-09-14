import math

if __name__ == "__main__":
    with open("rosalind_pper.txt") as f:
        n, k = [int(x) for x in f.readline().strip().split()]
    print((math.comb(n, k) * math.factorial(k)) % 1000000)
