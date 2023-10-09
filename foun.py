from math import log, factorial
from decimal import Decimal
from fractions import Fraction


def calculate_rec_annihilation(pop, gens, recAlleles):
    alleleSum = 2 * pop
    probs = []
    for i, recAllele in enumerate(recAlleles):
        probs.append([])
        recAlleleProb = {recAllele: Fraction(1, 1)}
        for _ in range(1, gens+1):
            newRecAlleleProb = {}
            for recAlleleInNewGen in range(1, alleleSum+1):
                for previous_k, previous_prob in recAlleleProb.items():
                    p = Fraction(previous_k, alleleSum)
                    q = Fraction(1, 1) - p
                    newRecAlleleProb[recAlleleInNewGen] = (
                        newRecAlleleProb.get(recAlleleInNewGen, Fraction(0, 1))
                        + (
                            previous_prob
                            * Fraction(
                                factorial(alleleSum),
                                factorial(recAlleleInNewGen) * factorial(alleleSum-recAlleleInNewGen)
                            )
                            * p**recAlleleInNewGen
                            * q**(alleleSum-recAlleleInNewGen)
                        )
                    )
            recAlleleProb = newRecAlleleProb
            zeroRecProb = Fraction(1, 1)
            for y in range(1, alleleSum+1):
                zeroRecProb -= recAlleleProb[y]
            probs[i].append(Decimal(zeroRecProb.numerator).log10()-Decimal(zeroRecProb.denominator).log10())
    return(probs)

if __name__ == "__main__":
    with open("inputfiles/rosalind_foun.txt") as f:
        n, m = [int(x) for x in f.readline().strip().split()]
        recAlleles = [int(x) for x in f.readline().strip().split()]
    probs = calculate_rec_annihilation(n, m, recAlleles)
    for i in range(m):
        for j in range(len(recAlleles)):
            print(probs[j][i], end=" ")
        print("")
