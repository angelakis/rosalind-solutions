from rosa_tools import transcribe_to_rna, reverse_and_complement, find_all_prots_of_reading_frame


def get_possible_prots_from_dna(dna):
    prots = []
    rna = transcribe_to_rna(dna)
    revRna = transcribe_to_rna(reverse_and_complement(dna))
    for i in range(3):
        prots += find_all_prots_of_reading_frame(rna[i:])
        prots += find_all_prots_of_reading_frame(revRna[i:])
    return(set(prots))

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_orf.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dnaString = fasta_dna_strings[key]
    possibleProts = get_possible_prots_from_dna(dnaString)
    print("\n".join(possibleProts))
