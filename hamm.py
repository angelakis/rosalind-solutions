def calculate_hamm_dist(dna1, dna2):
    hamm = 0
    for i in range(min(len(dna1), len(dna2))):
        if dna1[i] != dna2[i]:
            hamm += 1
    return(hamm)

if __name__ == "__main__":
    with open("rosalind_hamm.txt") as f:
        dna1 = f.readline().strip()
        dna2 = f.readline().strip()
    print(calculate_hamm_dist(dna1, dna2))
