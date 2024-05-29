
def shortest_good_subsequence(n, adjacency_matrix, m, path):
    graph = {}
    for i in range(n):
        graph[i+1] = [j+1 for j in range(n) if adjacency_matrix[i][j] == '1']

    def bfs(start, end):
        queue = [[start]]
        while queue:
            path = queue.pop(0)
            node = path[-1]
            if node == end:
                return path
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)

    shortest_path = []
    for i in range(m):
        for j in range(i+1, m):
            sub_path = bfs(path[i], path[j])
            if sub_path and sub_path == path[i:j+1] and len(sub_path) < len(shortest_path) or not shortest_path:
                shortest_path = sub_path

    return len(shortest_path), shortest_path

# Read input
n = int(input())
adjacency_matrix = [input().strip() for _ in range(n)]
m = int(input())
path = list(map(int, input().split()))

# Call the function and print the output
k, result = shortest_good_subsequence(n, adjacency_matrix, m, path)
print(k)
print(" ".join(map(str, result)))
