from math import comb

def calculate_dominant_phenotype(k, m, n):
    all_pairs = comb(k+m+n, 2)
    pairs_with_homoz_dom = all_pairs - comb(m+n, 2)  # an homozygous dominant ensures dominant allele
    pairs_with_heterozygous = comb(m, 2)
    pairs_with_heteroz_homoz_rec = comb(m+n, 2) - pairs_with_heterozygous - comb(n, 2)
    perc = (pairs_with_homoz_dom + pairs_with_heterozygous * 0.75 + pairs_with_heteroz_homoz_rec * 0.5) / all_pairs
    return perc

if __name__ == "__main__":
    with open("inputfiles/rosalind_iprb.txt") as f:
        k, m, n = [int(x) for x in f.readline().strip().split()]
    print(round(calculate_dominant_phenotype(k, m, n), 5))
