from math import log

def logs_of_prob_gc(dna, gcProbs):
    probs = []
    for prob in gcProbs:
        cumul_prob = log(1.0, 10)
        base_probs = {
            "C": prob/2,
            "G": prob/2,
            "A": (1-prob)/2,
            "T": (1-prob)/2,
        }
        for base in dna:
            cumul_prob += log(base_probs[base], 10)
        probs.append(cumul_prob)
    return(probs)

if __name__ == "__main__":
    with open("inputfiles/rosalind_prob.txt") as f:
        dna = f.readline().strip()
        gcProbs = list(map(float, f.readline().split()))
    print(" ".join(map(str, logs_of_prob_gc(dna, gcProbs))))
