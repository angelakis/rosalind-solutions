from math import sqrt


def freq_of_carriers(homozRecFreqs):
    """
    Because of hardy weinberg and using the prunett square:
    f(AA) + f(Aa) + f(aa) = p^2 + 2pq + q^2 = 1

    Then we just solve the quadratic equation for p and we calculate
    1-f(AA) = 1 - p^2 = 1 - (1-q)^2 where q^2 is the input freqs
    """
    freqs = []
    for f in homozRecFreqs:
        freqs.append(round(1-((1-sqrt(f)) ** 2), 3))
    return(freqs)

if __name__ == "__main__":
    with open("inputfiles/rosalind_afrq.txt") as f:
        homozRecFreqs = list(map(float, f.readline().split()))
    print(" ".join(map(str, freq_of_carriers(homozRecFreqs))))
