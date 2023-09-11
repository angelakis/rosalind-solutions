def find_consensus_and_matrix(fasta_dna_strings):
    dna_len = len(list(fasta_dna_strings.values())[0])
    profile_matrix = {"A": [0]*dna_len, "C": [0]*dna_len, "G": [0]*dna_len, "T": [0]*dna_len}
    for dna in fasta_dna_strings.values():
        for i, base in enumerate(dna):
            profile_matrix[base][i] += 1
    consensus = ""
    for i in range(dna_len):
        cur_max = max(profile_matrix["A"][i] ,profile_matrix["C"][i], profile_matrix["G"][i], profile_matrix["T"][i])
        for base in ("A", "C", "G", "T"):
            if profile_matrix[base][i] == cur_max:
                consensus += base
                break
    return(consensus, profile_matrix)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("rosalind_cons.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    consensus, profile_matrix = find_consensus_and_matrix(fasta_dna_strings)
    print(f'{consensus}\nA: {" ".join(map(str, profile_matrix["A"]))}\nC: {" ".join(map(str, profile_matrix["C"]))}\nG: {" ".join(map(str, profile_matrix["G"]))}\nT: {" ".join(map(str, profile_matrix["T"]))}')
