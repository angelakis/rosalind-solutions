from rosa_tools import is_own_reverse_complement

def find_restriction_sites(dna):
    restrictionSites = []
    for i in range(len(dna)):
        for j in range(i+4, min(i+13, len(dna)+1), 2):
            if is_own_reverse_complement(dna[i:j]):
                restrictionSites.append([i+1, j-i])
    return(restrictionSites)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_revp.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dnaString = fasta_dna_strings[key]
    restrictionSites = find_restriction_sites(dnaString)
    print("\n".join([f"{site[0]} {site[1]}" for site in restrictionSites]))
