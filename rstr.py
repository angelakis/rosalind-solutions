def calculate_equality_with_gc(dna, gcProb):
    cumul_prob = 1.0
    base_probs = {
        "C": gcProb/2,
        "G": gcProb/2,
        "A": (1-gcProb)/2,
        "T": (1-gcProb)/2,
    }
    for base in dna:
        cumul_prob *= base_probs[base]
    return(cumul_prob)

if __name__ == "__main__":
    with open("inputfiles/rosalind_rstr.txt") as f:
        firstLine = f.readline().split()
        n, gcProb = int(firstLine[0]), float(firstLine[1])
        dna = f.readline().strip()
    equalsProb = calculate_equality_with_gc(dna, gcProb)
    print(1 - (1 - equalsProb)**n)
