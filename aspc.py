import math

if __name__ == "__main__":
    with open("inputfiles/rosalind_aspc.txt") as f:
        n, m = [int(x) for x in f.readline().strip().split()]
    ss = 0
    for i in range(m, n+1):
        ss = (ss + math.comb(n, i)) % 1000000
    print(ss)
