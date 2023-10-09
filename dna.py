def count_dna_bases(dna):
    thymines = dna.count("T")
    adenines = dna.count("A")
    guanines = dna.count("G")
    cytosines = dna.count("C")
    return(adenines, cytosines, guanines, thymines)

if __name__ == "__main__":
    with open("inputfiles/rosalind_dna.txt") as f:
        dna = f.readline().strip()
    adenines, cytosines, guanines, thymines = count_dna_bases(dna)
    print(f"{adenines} {cytosines} {guanines} {thymines}")
