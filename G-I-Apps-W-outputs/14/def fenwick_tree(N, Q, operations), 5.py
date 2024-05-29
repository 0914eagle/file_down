
def fenwick_tree(N, Q, operations):
    def update(fenwick_tree, idx, delta):
        while idx < len(fenwick_tree):
            fenwick_tree[idx] += delta
            idx += idx & -idx
    
    def query(fenwick_tree, idx):
        total = 0
        while idx > 0:
            total += fenwick_tree[idx]
            idx -= idx & -idx
        return total
    
    fenwick_tree = [0] * (N + 1)
    results = []
    
    for op in operations:
        if op[0] == '+':
            i, delta = op[1], op[2]
            update(fenwick_tree, i + 1, delta)
        elif op[0] == '?':
            i = op[1]
            results.append(str(query(fenwick_tree, i)))
    
    return results

# Read input
N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]

# Call function and print results
results = fenwick_tree(N, Q, operations)
for res in results:
    print(res)
```
