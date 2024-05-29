
def update(bit, index, value):
    index += 1
    while index < len(bit):
        bit[index] += value
        index += index & -index

def query(bit, index):
    index += 1
    result = 0
    while index > 0:
        result += bit[index]
        index -= index & -index
    return result

def build_fenwick_tree(arr):
    bit = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        update(bit, i, arr[i])
    return bit

def fenwick_tree_operations(N, Q, operations):
    arr = [0] * N
    bit = build_fenwick_tree(arr)
    output = []
    for op in operations:
        if op[0] == '+':
            update(bit, int(op[1]), int(op[2]))
        elif op[0] == '?':
            output.append(query(bit, int(op[1])))
    return output

# Input processing
N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]

results = fenwick_tree_operations(N, Q, operations)
for result in results:
    print(result)
```
