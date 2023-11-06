def calculate_transi_transv_ratio(fasta_dna_strings):
    dnaStrings = list(fasta_dna_strings.values())
    transitions, transversions = 0, 0
    for i in range(len(dnaStrings[0])):
        base1, base2 = dnaStrings[0][i], dnaStrings[1][i]
        if base1 == base2:
            continue
        if (
            (base1 in ("A", "G") and base2 in ("C", "T"))
            or (base2 in ("A", "G") and base1 in ("C", "T"))
        ):
            transversions += 1
        else:
            transitions += 1
    return(transitions/transversions)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_tran.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    print(calculate_transi_transv_ratio(fasta_dna_strings))
