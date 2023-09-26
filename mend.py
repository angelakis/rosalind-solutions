from rosa_tools import parse_newick, TreeNode, genotypePairsOdds
from decimal import Decimal

class TreeNodeProbs(TreeNode):
    def __init__(self, val):
        self.odds = {}
        super().__init__(val)

def calculate_probs(tree_newick):
    tree = parse_newick(tree_newick, treeType=TreeNodeProbs)
    queue = [tree]
    while queue:
        curNode = queue.pop()
        if "" in (curNode.children[0].val, curNode.children[1].val):
            queue += [c for c in curNode.children if c.val == ""]
            if curNode.val == "":
                queue = [curNode] + queue
            continue
        if curNode.val == "depends":
            continue
        for i in range(2):
            if curNode.children[i].val != "depends":
                curNode.children[i].odds = {curNode.children[i].val: Decimal(1.0)}
        for genotype1, percentage1 in curNode.children[0].odds.items():
            for genotype2, percentage2 in curNode.children[1].odds.items():
                pair = "".join(sorted([genotype1, genotype2]))
                curNode.odds["AA"] = curNode.odds.get("AA", 0) + percentage1 * percentage2 * Decimal(genotypePairsOdds[pair][0])
                curNode.odds["Aa"] = curNode.odds.get("Aa", 0) + percentage1 * percentage2 * Decimal(genotypePairsOdds[pair][1])
                curNode.odds["aa"] = curNode.odds.get("aa", 0) + percentage1 * percentage2 * Decimal(genotypePairsOdds[pair][2])
        curNode.val = "depends"
    return(tree.odds)


if __name__ == "__main__":
    with open("rosalind_mend.txt") as f:
        tree = f.readline().strip()[:-1]
    probs = calculate_probs(tree)
    print(f"{probs['AA']} {probs['Aa']} {probs['aa']}")
