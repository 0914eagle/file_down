
import math

def distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])

def union(parent, rank, i, j):
    root_i = find_parent(parent, i)
    root_j = find_parent(parent, j)

    if rank[root_i] < rank[root_j]:
        parent[root_i] = root_j
    elif rank[root_i] > rank[root_j]:
        parent[root_j] = root_i
    else:
        parent[root_j] = root_i
        rank[root_i] += 1

def solve_aqueducts(n, s, t, q, hills, springs, towns):
    edges = []
    for i in range(n):
        for j in range(i+1, n):
            edges.append((i, j, distance(hills[i][0], hills[i][1], hills[j][0], hills[j][1])))

    edges.sort(key=lambda x: x[2])

    parent = [i for i in range(n)]
    rank = [0] * n

    total_length = 0
    aqueducts = 0

    for edge in edges:
        if aqueducts == n - t:
            break

        i, j, length = edge
        if length <= q:
            root_i = find_parent(parent, i)
            root_j = find_parent(parent, j)

            if root_i != root_j:
                union(parent, rank, i, j)
                total_length += length
                aqueducts += 1

    if aqueducts < n - t:
        return "IMPOSSIBLE"

    return "{:.6f}".format(total_length)

# Input parsing
n, s, t, q = map(int, input().split())
hills = [list(map(int, input().split())) for _ in range(n)]
springs = list(map(int, input().split()))
towns = list(map(int, input().split()))

print(solve_aqueducts(n, s, t, q, hills, springs, towns))
