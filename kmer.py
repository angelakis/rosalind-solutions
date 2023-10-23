import itertools

def tetra_nucleotide_composition(dna):
    kmers = {"".join(k): 0 for k in itertools.product("ACGT", repeat=4)}
    for i in range(len(dna)-3):
        kmers[dna[i:i+4]] += 1
    return(kmers)



if __name__ == "__main__":
    dnaString = ""
    with open("inputfiles/rosalind_kmer.txt") as f:
        for line in f.readlines():
            if line[0] != ">":
                dnaString += line.strip()
    print(" ".join(map(str, tetra_nucleotide_composition(dnaString).values())))
