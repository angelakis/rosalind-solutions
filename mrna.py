rna_codons = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}

def calculate_reverse_rna_codons(codon_dict):
    reverse_codon_dict = {}
    for codon, aminoAcid in codon_dict.items():
        reverse_codon_dict[aminoAcid] = reverse_codon_dict.get(aminoAcid, 0) + 1
    return(reverse_codon_dict)

def count_possible_rna_strings(protein):
    rna_strings = 1
    reverse_codon_dict = calculate_reverse_rna_codons(rna_codons)
    for i in range(len(protein)):
        rna_strings = (rna_strings * reverse_codon_dict[protein[i]]) % (10**6)
    return(rna_strings * reverse_codon_dict["Stop"] % (10**6))

if __name__ == "__main__":
    with open("inputfiles/rosalind_mrna.txt") as f:
        protein = f.readline().strip()
    print(count_possible_rna_strings(protein))
