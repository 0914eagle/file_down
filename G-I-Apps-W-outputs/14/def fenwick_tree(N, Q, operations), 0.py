
def fenwick_tree(N, Q, operations):
    tree = [0] * (N + 1)

    def update(index, delta):
        while index <= N:
            tree[index] += delta
            index += index & -index

    def query(index):
        result = 0
        while index > 0:
            result += tree[index]
            index -= index & -index
        return result

    for op in operations:
        if op[0] == '+':
            i, delta = op[1], op[2]
            update(i + 1, delta)
        else:  # '?' query
            i = op[1]
            print(query(i))

# Read input
N, Q = map(int, input().split())
operations = []
for _ in range(Q):
    operation = input().split()
    if operation[0] == '+':
        operations.append((operation[0], int(operation[1]), int(operation[2]))
    else:  # '?' query
        operations.append((operation[0], int(operation[1]))

# Solve
fenwick_tree(N, Q, operations)
```
