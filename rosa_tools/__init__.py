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
