import itertools
import math

if __name__ == "__main__":
    with open("inputfiles/rosalind_perm.txt") as f:
        n = int(f.readline().strip())
    perms = list(itertools.permutations(list(range(1, n+1))))
    print(math.factorial(n))
    for p in perms:
        print(" ".join(map(str, p)))
