
# Fenwick Tree implementation
def query(tree, idx):
    result = 0
    while idx > 0:
        result += tree[idx]
        idx -= idx & -idx
    return result

def update(tree, idx, delta):
    while idx < len(tree):
        tree[idx] += delta
        idx += idx & -idx

# Main function
def fenwick_tree_operations(N, Q, operations):
    tree = [0] * (N + 1)
    for op in operations:
        if op[0] == '+':
            i, delta = int(op[1]), int(op[2])
            update(tree, i + 1, delta)
        elif op[0] == '?':
            i = int(op[1])
            print(query(tree, i))

# Input processing
N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]

# Run the main function
fenwick_tree_operations(N, Q, operations)
```
