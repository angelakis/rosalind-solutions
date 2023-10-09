from decimal import Decimal

from rosa_tools import aaMonoisotopeMass

def calculate_prot_weight(prot):
    weight = sum(Decimal(aaMonoisotopeMass[aa]) for aa in prot)
    return(weight)

if __name__ == "__main__":
    with open("inputfiles/rosalind_prtm.txt") as f:
        prot = f.readline().strip()
    print(calculate_prot_weight(prot))
