
def update(fenwick_tree, i, delta):
    while i < len(fenwick_tree):
        fenwick_tree[i] += delta
        i += i & -i

def query(fenwick_tree, i):
    total = 0
    while i > 0:
        total += fenwick_tree[i]
        i -= i & -i
    return total

def fenwick_tree_operations(N, Q, operations):
    fenwick_tree = [0] * (N + 1)
    output = []

    for op in operations:
        if op[0] == '+':
            update(fenwick_tree, int(op[1]), int(op[2]))
        elif op[0] == '?':
            output.append(str(query(fenwick_tree, int(op[1])))

    return output

# Read input
N, Q = map(int, input().split())
operations = []
for _ in range(Q):
    operations.append(input().split())

# Perform operations and output results
results = fenwick_tree_operations(N, Q, operations)
for res in results:
    print(res)
