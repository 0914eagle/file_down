
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def calc(n, p, k, t):
    total = 0
    for i in range(n):
        total += (t[i] - total) * (100 + i * p) / 100
    total += (k - total) * (100 + n * p) / 100
    return total

def binary_search(l, r):
    while l < r:
        m = (l + r) // 2
        if calc(n, p, k, t) > m:
            r = m
        else:
            l = m + 1
    return l

print(binary_search(0, k))

