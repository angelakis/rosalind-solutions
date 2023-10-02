import requests

def get_prot_sequences(prots):
    seqs = []
    for prot in prots:
        r = requests.get(f"http://www.uniprot.org/uniprot/{prot}.fasta")
        breakpoint()
        seqs.append(r.text.split('\n')[1])
    return(seqs)



if __name__ == "__main__":
    with open("rosalind_mprt.txt") as f:
        prots = [prot.strip() for prot in f.readlines()]
    protSequences = get_prot_sequences(prots)
    # print(round(calculate_dominant_phenotype(k, m, n), 5))
