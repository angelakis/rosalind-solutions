import itertools

if __name__ == "__main__":
    with open("inputfiles/rosalind_sign.txt") as f:
        n = int(f.readline().strip())
    perms = list(itertools.permutations(list(range(1, n+1))))
    signs = list(itertools.product([1,-1], repeat=n))
    print(len(perms) * len(signs))
    for p in perms:
        for s in signs:
            print(" ".join([str(x*y) for (x,y) in zip(p, s)]))
