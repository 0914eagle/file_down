
def solve(m, n, a, b):
    a.sort()
    b.sort()
    res = 0
    i = 0
    j = 0
    while i < m and j < n:
        if a[i] < b[j]:
            res += a[i]
            i += 1
        else:
            res += b[j]
            j += 1
    return res

m, n = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(solve(m, n, a, b))

