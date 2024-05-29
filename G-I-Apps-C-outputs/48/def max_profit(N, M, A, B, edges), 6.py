
def max_profit(N, M, A, B, edges):
    def dfs(node, visited):
        visited.add(node)
        sub_score = abs(B[node])

        for edge in edges[node]:
            next_node = edge[0]
            if next_node not in visited:
                sub_score += dfs(next_node, visited)

        return sub_score

    profits = []

    for i in range(N):
        visited = set()
        score = 0

        for j in range(N):
            if j != i and j not in visited:
                score += dfs(j, visited)

        profits.append(score - A[i])

    return max(profits)

# Sample Input
N, M = 4, 4
A = [4, 1, 2, 3]
B = [0, 2, -3, 1]
edges = {1: [(2,)], 2: [(3,), (1,)], 3: [(4,), (2,)], 4: [(3,)]}

print(max_profit(N, M, A, B, edges))
