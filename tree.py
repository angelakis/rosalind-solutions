def find_islands(undir_graph):
    islands = []
    visited = {node: False for node in list(range(1, len(undir_graph)+1))}
    queue = [1]
    cur_island = [1]
    visited[1] = True
    while True:
        if not queue:
            islands.append(cur_island)
            for n, is_visited in visited.items():
                if not is_visited:
                    cur_island = [n]
                    queue = [n]
                    visited[n] = True
                    break
            if not queue:
                break
        cur = queue.pop()
        for neighbour in undir_graph[cur]:
            if not visited[neighbour]:
                queue.append(neighbour)
                visited[neighbour] = True
                cur_island.append(neighbour)
    return(islands)

if __name__ == "__main__":
    edges = []
    with open("inputfiles/rosalind_tree.txt") as f:
        lines = f.readlines()
        n = int(lines[0].strip())
        for l in lines[1:]:
            edges.append(map(int, l.strip().split()))
    undir_graph = {k: [] for k in list(range(1, n+1))}
    for (x, y) in edges:
        undir_graph[x] += [y]
        undir_graph[y] += [x]
    islands = find_islands(undir_graph)
    print(len(islands)-1)
