from decimal import Decimal

def calculate_distance_matrix(fasta_dna_strings):
    dnaLen = len(fasta_dna_strings[0])
    matrixLen = len(fasta_dna_strings)
    dists = [matrixLen * [0] for _ in range(matrixLen)]
    for i in range(matrixLen-1):
        for j in range(i+1, matrixLen):
            hamm = 0
            for w in range(dnaLen):
                if fasta_dna_strings[i][w] != fasta_dna_strings[j][w]:
                    hamm += 1
            dists[i][j] = dists[j][i] = hamm / Decimal(dnaLen)
    return(dists)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_pdst.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    distances = calculate_distance_matrix(list(fasta_dna_strings.values()))
    print("\n".join([" ".join([str(dist) for dist in row]) for row in distances]))
