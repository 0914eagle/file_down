
def find_max_profit(N, M, A, B, edges):
    import networkx as nx

    G = nx.Graph()
    for i in range(1, N+1):
        G.add_node(i, A=A[i-1], B=B[i-1])
    for i in range(1, M+1):
        u, v = edges[i-1]
        G.add_edge(u, v)

    components = list(nx.connected_components(G))

    max_profit = 0
    for component in components:
        profit = sum(G.nodes[node]['B'] for node in component) - sum(G.nodes[node]['A'] for node in component)
        max_profit = max(max_profit, profit)

    return max_profit


# Sample Input
N, M = 4, 4
A = [4, 1, 2, 3]
B = [0, 2, -3, 1]
edges = [(1, 2), (2, 3), (3, 4), (4, 2)]

print(find_max_profit(N, M, A, B, edges))
