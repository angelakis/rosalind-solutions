from rosa_tools import reverse_and_complement, calculate_hamm_dist


def correct_mistakes(fasta_dna_strings):
    archived = archive_dnas(fasta_dna_strings)
    mistakes = []
    for dna, (num, original) in archived.items():
        if not original or num > 1:
            continue
        for correctDna, (num, _) in archived.items():
            if num <= 1:
                continue
            if calculate_hamm_dist(dna, correctDna) == 1:
                mistakes.append((dna, correctDna))
                break
    return(mistakes)

def archive_dnas(fasta_dna_strings):
    archived = {}
    for dna in fasta_dna_strings.values():
        revDna = reverse_and_complement(dna)
        archived[dna] = (archived.get(dna, [0, None])[0] + 1, True)
        archived[revDna] = (archived.get(revDna, [0, None])[0] + 1, archived.get(revDna, [None, False])[1])
    return(archived)

if __name__ == "__main__":
    fasta_dna_strings = {}
    with open("inputfiles/rosalind_corr.txt") as f:
        for line in f.readlines():
            if line[0] == ">":
                key = line.split()[0][1:]
            else:
                fasta_dna_strings[key] = fasta_dna_strings.get(key, "") + line.strip()
    mistakes = correct_mistakes(fasta_dna_strings)
    print("\n".join(f"{bef}->{aft}" for (bef, aft) in mistakes))
