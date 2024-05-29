
def fenwick_tree(N, Q, operations):
    def query(bit, i):
        res = 0
        i += 1
        while i > 0:
            res += bit[i]
            i -= i & -i
        return res

    def update(bit, i, delta):
        i += 1
        while i <= N:
            bit[i] += delta
            i += i & -i

    bit = [0] * (N + 1)
    result = []
    
    for op in operations:
        if op[0] == '+':
            update(bit, int(op[1]), int(op[2]))
        elif op[0] == '?':
            result.append(str(query(bit, int(op[1])))

    return result

# Input processing
N, Q = map(int, input().split())
operations = [input().split() for _ in range(Q)]

# Solve using Fenwick Tree
output = fenwick_tree(N, Q, operations)

# Output results
for res in output:
    print(res)
