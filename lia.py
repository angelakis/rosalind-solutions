from math import comb

# class Factor:
#     def __init__(self, alleles):
#         alleles = sorted(alleles)
#         self.alleles = [alleles[0], alleles[1]]

#     def __str__(self):
#         return "".join(self.alleles)

#     def __lt__(self, other):
#         return(str(self) < str(other))

# class Genome:
#     def __init__(self, genome):
#         self.factors = []
#         alleles = {}
#         for allele in genome:
#             alleles[allele.lower()] = sorted(alleles.get(allele.lower(), []) + [allele])
#         for k, v in alleles.items():
#             self.factors.append(Factor(v))
#         self.factors = sorted(self.factors)

#     def __str__(self):
#         repr = ""
#         for f in self.factors:
#             repr += "".join(f.alleles)
#         return(repr)

#     def __hash__(self):
#         return hash(str(self))

#     def __repr__(self):
#         return str(self)

#     def __eq__(self, other):
#         return str(self) == str(other)

# def calculate_genomes_percentages(parent1, parent2=Genome("AaBb")):
#     genomes = {}
#     for i in range(len(parent1.factors)):
#         for j in range(len(parent2.factors)):
#             for x in range(2):
#                 for y in range(2):
#                     genome = Genome(
#                         parent1.factors[0].alleles[i]
#                         + parent1.factors[1].alleles[j]
#                         + parent2.factors[0].alleles[x]
#                         + parent2.factors[1].alleles[y]
#                     )
#                     genomes[genome] = genomes.get(genome, 0) + (1/16)
#     return(genomes)

# def calculate_chance_for_AaBb(k, n):
#     ancestor = Genome("AaBb")
#     print(ancestor)
#     children_genomes_chances = calculate_genomes_percentages(ancestor)
#     print(sum(children_genomes_chances.values()))
#     for k in range(2, k+1):
#         new_children_genomes_chances = {}
#         for child, chance in children_genomes_chances.items():
#             print(child, chance)
#             percentages = calculate_genomes_percentages(child)
#             print(percentages)
#             print(new_children_genomes_chances)
#             new_children_genomes_chances = {k: new_children_genomes_chances.get(k, 0.0) + chance * percentages.get(k, 0.0) for k in children_genomes_chances.keys()}
#             print(new_children_genomes_chances)
#         children_genomes_chances = new_children_genomes_chances
#         print(sum(children_genomes_chances.values()))
#     return(children_genomes_chances)


def calculate_chance_for_AaBb(k, n):
    prob_sum = 1.0
    children = 2**k
    for i in range(0, n):
        prob_sum -= comb(children, i) * (0.25**i) * (0.75**(children-i))
    return prob_sum

if __name__ == "__main__":
    with open("inputfiles/rosalind_lia.txt") as f:
        k, n = [int(x) for x in f.readline().strip().split()]
    breakpoint()
    print(calculate_chance_for_AaBb(k, n))
