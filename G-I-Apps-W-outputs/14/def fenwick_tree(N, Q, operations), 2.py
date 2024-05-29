
def fenwick_tree(N, Q, operations):
    def update_tree(index, delta):
        index += 1
        while index <= N:
            tree[index] += delta
            index += index & -index

    def query_prefix_sum(index):
        index += 1
        result = 0
        while index > 0:
            result += tree[index]
            index -= index & -index
        return result

    tree = [0] * (N + 1)

    for op in operations:
        if op[0] == '+':
            update_tree(int(op[1]), int(op[2]))
        elif op[0] == '?':
            print(query_prefix_sum(int(op[1])))

N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]
fenwick_tree(N, Q, operations)
```
