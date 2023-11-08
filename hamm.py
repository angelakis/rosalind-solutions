from rosa_tools import calculate_hamm_dist


if __name__ == "__main__":
    with open("inputfiles/rosalind_hamm.txt") as f:
        dna1 = f.readline().strip()
        dna2 = f.readline().strip()
    print(calculate_hamm_dist(dna1, dna2))
