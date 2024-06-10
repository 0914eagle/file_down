
def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union(parent, x, y):
    x = find_parent(parent, x)
    y = find_parent(parent, y)
    if x < y:
        parent[y] = x
    else:
        parent[x] = y

def kruskal(graph, n, insecure_buildings):
    parent = [i for i in range(n + 1)]
    result = 0
    for edge in graph:
        u, v, cost = edge
        if find_parent(parent, u) != find_parent(parent, v):
            if u in insecure_buildings or v in insecure_buildings:
                continue
            union(parent, u, v)
            result += cost
    return result

def main():
    n, m, p = map(int, input().split())
    insecure_buildings = set(map(int, input().split()))
    graph = []
    for _ in range(m):
        x, y, cost = map(int, input().split())
        graph.append((x, y, cost))
    graph.sort(key=lambda x: x[2])
    result = kruskal(graph, n, insecure_buildings)
    print(result if result > 0 else "impossible")

if __name__ == "__main__":
    main()

