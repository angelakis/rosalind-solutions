def reverse_and_complement(dna):
    complements = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C",
    }
    transTable = str.maketrans(complements)
    complementDna = dna[::-1].translate(transTable)
    return(complementDna)

if __name__ == "__main__":
    with open("rosalind_revc.txt") as f:
        dna = f.readline().strip()
    print(reverse_and_complement(dna))
