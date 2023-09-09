from math import comb

def dominant_phenotype_avg(x1, x2, x3, x4, x5):
    avg = 2 * (x1 + x2 + x3 + x4*0.75 + x5*0.5)
    return avg

if __name__ == "__main__":
    with open("rosalind_iev.txt") as f:
        x1, x2, x3, x4, x5, x6 = [int(x) for x in f.readline().strip().split()]
    print(dominant_phenotype_avg(x1, x2, x3, x4, x5))
