def calculate_overlap_graph(fasta_dna_strings):
    edges = []
    for label_suff, dna_suff in fasta_dna_strings.items():
        for label_pref, dna_pref in fasta_dna_strings.items():
            if label_pref == label_suff:
                continue
            if dna_suff[-3:] == dna_pref[:3]:
                edges.append((label_suff, label_pref))
    return(edges)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_grph.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    for edge in calculate_overlap_graph(fasta_dna_strings):
        print(" ".join(edge))
