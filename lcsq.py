def find_longest_common_subsequence(dna1, dna2):
    lcsTable = [[0] * (len(dna2)+1) for _ in range(len(dna1)+1)]
    for i in range(1, len(dna1)+1):
        for j in range(1, len(dna2)+1):
            if dna1[i-1] == dna2[j-1]:
                lcsTable[i][j] = lcsTable[i-1][j-1] + 1
            else:
                lcsTable[i][j] = max(lcsTable[i-1][j], lcsTable[i][j-1])
    lcs = ""
    i, j = len(dna1), len(dna2)
    while i > 0 and j > 0:
        if dna1[i-1] == dna2[j-1]:
            lcs = dna1[i-1] + lcs
            if lcsTable[i][j] == 1:
                break
            i, j = i-1, j-1
        else:
            if lcsTable[i-1][j] > lcsTable[i][j-1]:
                i -= 1
            else:
                j -= 1
    return(lcs)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_lcsq.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dna1, dna2 = fasta_dna_strings.values()
    print(find_longest_common_subsequence(dna1, dna2))
