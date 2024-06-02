
def lexicographically_maximal_permutation(n, m, p, swaps):
    parent = list(range(n))
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        x_root = find(x)
        y_root = find(y)
        if x_root == y_root:
            return
        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    for a, b in swaps:
        union(a - 1, b - 1)

    groups = {}
    for i in range(n):
        root = find(i)
        if root not in groups:
            groups[root] = []
        groups[root].append(i)

    result = [0] * n
    for root, group in groups.items():
        group.sort()
        for i, val in enumerate(group):
            result[val] = group[-i - 1] + 1

    return result

# Input parsing
n, m = map(int, input().split())
p = list(map(int, input().split()))
swaps = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
result = lexicographically_maximal_permutation(n, m, p, swaps)
print(*result)
