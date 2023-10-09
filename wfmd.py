from math import comb


def calculate_genetic_drift(pop, domAlleles, gens, recAlleleMin):
    alleleSum = 2 * pop
    recAlleleProb = {alleleSum - domAlleles: 1.0}
    for _ in range(1, gens+1):
        newRecAlleleProb = {}
        for recAlleleInNewGen in range(1, alleleSum+1):
            for previous_k, previous_prob in recAlleleProb.items():
                p = previous_k / alleleSum
                q = 1 - p
                newRecAlleleProb[recAlleleInNewGen] = (
                    newRecAlleleProb.get(recAlleleInNewGen, 0)
                    + (
                        previous_prob
                        * comb(alleleSum, recAlleleInNewGen)
                        * p**recAlleleInNewGen
                        * q**(alleleSum-recAlleleInNewGen)
                    )
                )
        recAlleleProb = newRecAlleleProb
        prob = 0
        for i in range(recAlleleMin, alleleSum+1):
            prob += recAlleleProb[i]
    return(prob)

if __name__ == "__main__":
    with open("inputfiles/rosalind_wfmd.txt") as f:
        n, m, g, k = [int(x) for x in f.readline().strip().split()]
    print(round(calculate_genetic_drift(n, m, g, k), 3))
