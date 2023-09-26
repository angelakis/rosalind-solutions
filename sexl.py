from decimal import Decimal


if __name__ == "__main__":
    """
    We are given the f(a) for the males and looking for the f(Aa) for the females.

    For the females we have f(AA) + f(Aa) + f(aa) = p^2 + 2pq + q^2 = 1. But the f(a) in the males
    must be the same as f(a) for the females so q = f(a), so we are looking for 2pq and of course
    p + q = 1.
    """
    with open("rosalind_sexl.txt") as f:
        recMales = list(map(Decimal, f.readline().split()))
    print(" ".join(map(str, [2 * q * (1-q) for q in recMales])))
