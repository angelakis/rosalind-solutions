from rosa_tools import (
    rna_codons, translate_to_prot, transcribe_to_rna
)

def remove_introns(dna, intron_sequences):
    for intron_sequence in intron_sequences:
        dna = dna.replace(intron_sequence, "")
    return(dna)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("rosalind_splc.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dnas = list(fasta_dna_strings.values())
    removed_dna = remove_introns(dnas[0], dnas[1:])
    print(translate_to_prot(transcribe_to_rna(removed_dna)))
