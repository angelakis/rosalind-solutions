def transcribe_to_rna(dna):
    rna = dna.replace("T", "U")
    return(rna)

if __name__ == "__main__":
    with open("rosalind_rna.txt") as f:
        dna = f.readline().strip()
    print(transcribe_to_rna(dna))
