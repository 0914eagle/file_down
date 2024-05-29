
def query_fenwick_tree(arr, idx):
    idx += 1
    res = 0
    while idx > 0:
        res += arr[idx - 1]
        idx -= idx & -idx
    return res

def update_fenwick_tree(arr, idx, delta):
    idx += 1
    while idx <= len(arr):
        arr[idx - 1] += delta
        idx += idx & -idx

N, Q = map(int, input().split())
arr = [0] * N

for _ in range(Q):
    op = input().split()
    if op[0] == '+':
        update_fenwick_tree(arr, int(op[1]), int(op[2]))
    elif op[0] == '?':
        idx = int(op[1])
        print(query_fenwick_tree(arr, idx))

# Sample Input
# 10 4
# + 7 23
# ? 8
# + 3 17
# ? 8
```
