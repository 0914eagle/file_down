
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def find_index(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1

def solve(a, b):
    res = 0
    for i in range(n):
        if a[i] != 0:
            continue
        idx = find_index(b, i+1)
        res += idx + 1
        a[i] = i+1
        b = b[idx+1:] + b[:idx+1]
    return res

print(solve(a, b))

