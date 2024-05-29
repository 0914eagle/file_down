
def update(fenwick_tree, i, delta):
    while i < len(fenwick_tree):
        fenwick_tree[i] += delta
        i += i & -i

def prefix_sum(fenwick_tree, i):
    result = 0
    while i > 0:
        result += fenwick_tree[i]
        i -= i & -i
    return result

def build_fenwick_tree(size):
    return [0] * (size + 1)

def fenwick_tree_operations(N, Q, operations):
    fenwick_tree = build_fenwick_tree(N)
    result = []

    for op in operations:
        if op[0] == '+':
            i, delta = int(op[1]), int(op[2])
            update(fenwick_tree, i + 1, delta)
        elif op[0] == '?':
            i = int(op[1])
            result.append(prefix_sum(fenwick_tree, i))

    return result

# Input parsing
N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]

# Perform operations
results = fenwick_tree_operations(N, Q, operations)

# Output results
for res in results:
    print(res)
```
