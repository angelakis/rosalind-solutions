from re import finditer

import requests


def get_prot_sequences(prots):
    seqs = []
    for prot in prots:
        protId = prot.split('_')[0]
        r = requests.get(f"http://www.uniprot.org/uniprot/{protId}.fasta")
        r.raise_for_status()
        seqs.append("".join(r.text.split('\n')[1:]))
    return(seqs)

# Can't use this because we need also overlapping
# def get_locations_by_regex(regex_pattern, text):
#     locs = []
#     for match in finditer(regex_pattern, text):
#         locs.append(match.span()[0] + 1)
#     return(locs)

def get_nGlycosylation_locations(protSeq):
    locs = []
    for i in range(len(protSeq)-3):
        if (
            protSeq[i] == 'N'
            and protSeq[i+1] != 'P'
            and protSeq[i+2] in ('S', 'T')
            and protSeq[i+3] != 'P'
        ):
            locs.append(i + 1)
    return(locs)

if __name__ == "__main__":
    with open("rosalind_mprt.txt") as f:
        prots = [prot.strip() for prot in f.readlines()]
    protSequences = get_prot_sequences(prots)
    for i, protSeq in enumerate(protSequences):
        locs = get_nGlycosylation_locations(protSeq)
        if locs:
            print(prots[i])
            print(" ".join(map(str, locs)))
