from math import factorial

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_pmch.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    dnaString = fasta_dna_strings[key]
    a, c = (dnaString.count("A"), dnaString.count("C"))
    print(factorial(a)*factorial(c))
