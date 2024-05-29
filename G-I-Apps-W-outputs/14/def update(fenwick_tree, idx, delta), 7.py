
def update(fenwick_tree, idx, delta):
    idx += 1
    while idx < len(fenwick_tree):
        fenwick_tree[idx] += delta
        idx += idx & -idx

def query(fenwick_tree, idx):
    idx += 1
    result = 0
    while idx > 0:
        result += fenwick_tree[idx]
        idx -= idx & -idx
    return result

def fenwick_tree_operations(N, Q, operations):
    fenwick_tree = [0] * (N + 1)
    output = []

    for op in operations:
        cmd, i, *rest = op.split()
        i = int(i)
        if cmd == '+':
            delta = int(rest[0])
            update(fenwick_tree, i, delta)
        elif cmd == '?':
            output.append(query(fenwick_tree, i))

    return output

# Input parsing
N, Q = map(int, input().split())
operations = [input() for _ in range(Q)]

output = fenwick_tree_operations(N, Q, operations)

for res in output:
    print(res)
```
