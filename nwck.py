from rosa_tools import parse_newick


def calculate_distances(trees, ends):
    distances = []
    for i, tree in enumerate(trees):
        cur_tree = parse_newick(tree)
        cur_dist = None
        queue = [cur_tree]
        while True:
            cur_node = queue.pop()
            if cur_node.val in ends[i]:
                break
            queue += cur_node.children
        queue = [(cur_node, 0)]
        cur_node.visited = True
        while True:
            (cur_node, dist) = queue.pop()
            if cur_node.val in ends[i] and dist:
                distances.append(dist)
                break
            neighbours = [c for c in cur_node.children + [cur_node.parent] if c and not c.visited]
            for neighbour in neighbours:
                neighbour.visited = True
                queue.append((neighbour, dist+1))
    return(distances)


if __name__ == "__main__":
    trees = []
    ends = []
    with open("inputfiles/rosalind_nwck.txt") as f:
        for line in f:
            if line.strip() == "":
                continue
            elif line[-2] == ";":
                trees.append(line.strip()[:-1])
            else:
                ends.append(line.strip().split())
    distances = calculate_distances(trees, ends)
    print(" ".join(map(str, distances)))
