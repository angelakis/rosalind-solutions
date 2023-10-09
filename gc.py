def find_highest_gc(fasta_dna_strings):
    highest_gc = 0
    highest_label = ""
    for label, dna_string in fasta_dna_strings.items():
        gc = (dna_string.count("G") + dna_string.count("C")) / len(dna_string)
        if gc > highest_gc:
            highest_gc = gc
            highest_label = label
    return(highest_label, 100 * highest_gc)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_gc.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    label, gc =  find_highest_gc(fasta_dna_strings)
    print(f"{label}\n{gc}")
