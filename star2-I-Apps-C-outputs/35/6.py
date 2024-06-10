
n = int(input())
a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]

def find_index(arr, target):
    for i, val in enumerate(arr):
        if val == target:
            return i
    return -1

def find_min_ops(a, b):
    ops = 0
    for i in range(1, n+1):
        idx_a = find_index(a, i)
        idx_b = find_index(b, i)
        if idx_a != -1:
            ops += idx_a
            a[idx_a] = 0
        elif idx_b != -1:
            ops += idx_b + 1
            b[idx_b] = 0
    return ops

print(find_min_ops(a, b))

