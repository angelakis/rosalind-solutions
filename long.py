def fragment_assembly_guaranteed_half(fastaDnaStrings):
    dnas = fastaDnaStrings.copy()
    reassembledDna = dnas.popitem()[1]
    while dnas:
        for label, dna in dnas.copy().items():
            if dna in reassembledDna:
                dnas.pop(label)
                continue
            prefix = dna[:len(dna)//3]
            prefixInd = reassembledDna.find(prefix)
            suffix = dna[2*(len(dna)//3):]
            suffixInd = reassembledDna.find(suffix)
            if prefixInd == -1 and suffixInd == -1:
                continue
            if prefixInd != -1:
                reassembledDna += dna[len(reassembledDna)-prefixInd:]
            elif suffixInd != -1:
                reassembledDna = dna[:len(dna) - len(suffix) - suffixInd] + reassembledDna
            dnas.pop(label)
    return(reassembledDna)


if __name__ == "__main__":
    fastaDnaStrings = {}
    with open("inputfiles/rosalind_long.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fastaDnaStrings[key] = fastaDnaStrings.get(key, "") + line.strip()
    dna = fragment_assembly_guaranteed_half(fastaDnaStrings)
    print(dna)
