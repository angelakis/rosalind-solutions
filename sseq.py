def find_subsequence_location(dna, subSeq):
    indices = []
    indexSearched = 0
    for i, base in enumerate(dna):
        if base != subSeq[indexSearched]:
            continue
        indices.append(i+1)
        if len(indices) == len(subSeq):
            break
        indexSearched += 1
    return(indices)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_sseq.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    subSeq = fasta_dna_strings[key]
    fasta_dna_strings.pop(key)
    dna = list(fasta_dna_strings.values())[0]
    indices = find_subsequence_location(dna, subSeq)
    print(" ".join(map(str, indices)))
