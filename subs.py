def find_substr_locs(dna, dnaSub):
    locs = []
    for i in range(len(dna)):
        if dna[i:len(dnaSub)+i] == dnaSub:
            locs.append(i+1)
    return(locs)

if __name__ == "__main__":
    with open("rosalind_subs.txt") as f:
        dna = f.readline().strip()
        dnaSub = f.readline().strip()
    locs = find_substr_locs(dna, dnaSub)
    print(" ".join(map(str, locs)))
