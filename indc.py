from math import log, factorial
from decimal import Decimal
from fractions import Fraction


def calculate_prob_for_common_chromosomes(n):
    probs = []
    prob_sum = Fraction(1, 1)
    for i in range(1, n+1):
        prob_sum -= Fraction(factorial(n), factorial(i-1) * factorial(n-i+1)) * Fraction(1, 2**n)
        probs.append(round(Decimal(prob_sum.numerator).log10()-Decimal(prob_sum.denominator).log10(), 3) + 0)
    return probs

if __name__ == "__main__":
    with open("inputfiles/rosalind_indc.txt") as f:
        n = int(f.readline().strip())
    print(" ".join(map(str, calculate_prob_for_common_chromosomes(2*n))))
