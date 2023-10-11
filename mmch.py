from math import comb, factorial

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_mmch.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dnaString = fasta_dna_strings[key]
    a, c, u, g = (
        dnaString.count("A"),
        dnaString.count("C"),
        dnaString.count("U"),
        dnaString.count("G"),
    )
    print(factorial(min(a,u)) * comb(max(a,u), min(a,u)) * factorial(min(c,g)) * comb(max(c,g), min(c,g)))
