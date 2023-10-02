rna_codons = {
    "UUU": "F",
    "CUU": "L",
    "AUU": "I",
    "GUU": "V",
    "UUC": "F",
    "CUC": "L",
    "AUC": "I",
    "GUC": "V",
    "UUA": "L",
    "CUA": "L",
    "AUA": "I",
    "GUA": "V",
    "UUG": "L",
    "CUG": "L",
    "AUG": "M",
    "GUG": "V",
    "UCU": "S",
    "CCU": "P",
    "ACU": "T",
    "GCU": "A",
    "UCC": "S",
    "CCC": "P",
    "ACC": "T",
    "GCC": "A",
    "UCA": "S",
    "CCA": "P",
    "ACA": "T",
    "GCA": "A",
    "UCG": "S",
    "CCG": "P",
    "ACG": "T",
    "GCG": "A",
    "UAU": "Y",
    "CAU": "H",
    "AAU": "N",
    "GAU": "D",
    "UAC": "Y",
    "CAC": "H",
    "AAC": "N",
    "GAC": "D",
    "UAA": "Stop",
    "CAA": "Q",
    "AAA": "K",
    "GAA": "E",
    "UAG": "Stop",
    "CAG": "Q",
    "AAG": "K",
    "GAG": "E",
    "UGU": "C",
    "CGU": "R",
    "AGU": "S",
    "GGU": "G",
    "UGC": "C",
    "CGC": "R",
    "AGC": "S",
    "GGC": "G",
    "UGA": "Stop",
    "CGA": "R",
    "AGA": "R",
    "GGA": "G",
    "UGG": "W",
    "CGG": "R",
    "AGG": "R",
    "GGG": "G",
}

genotypePairsOdds = {
    "AAAA": (1.0, 0.0, 0.0),
    "AAAa": (0.5, 0.5, 0.0),
    "AAaa": (0.0, 1.0, 0.0),
    "AaAa": (0.25, 0.5, 0.25),
    "Aaaa": (0.0, 0.5, 0.5),
    "aaaa": (0.0, 0.0, 1.0),
}

aaMonoisotopeMass = {
    "A":   71.03711,
    "C":   103.00919,
    "D":   115.02694,
    "E":   129.04259,
    "F":   147.06841,
    "G":   57.02146,
    "H":   137.05891,
    "I":   113.08406,
    "K":   128.09496,
    "L":   113.08406,
    "M":   131.04049,
    "N":   114.04293,
    "P":   97.05276,
    "Q":   128.05858,
    "R":   156.10111,
    "S":   87.03203,
    "T":   101.04768,
    "V":   99.06841,
    "W":   186.07931,
    "Y":   163.06333,
}

waterMonoisotopeMass = 18.01056


def translate_to_prot(rna):
    prot = ""
    for i in range(0, len(rna), 3):
        cur_amino_acid = rna_codons[rna[i:i+3]]
        if cur_amino_acid == "Stop":
            break
        prot += cur_amino_acid
    return(prot)


def transcribe_to_rna(dna):
    rna = dna.replace("T", "U")
    return(rna)


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.parent = None
        self.children = []
        self.visited = False

def parse_newick(newick_str, treeType=TreeNode):
    stack = [treeType('')]
    current_node = None
    for char in newick_str:
        if char == '(':
            if current_node:
                stack.append(current_node)
            current_node = treeType('')
        elif char == ')':
            parent = stack.pop()
            current_node.parent = parent
            parent.children.append(current_node)
            current_node = parent
        elif char == ',':
            parent = stack[-1]
            current_node.parent = parent
            parent.children.append(current_node)
            current_node = treeType('')
        else:
            current_node.val += char
    return current_node
