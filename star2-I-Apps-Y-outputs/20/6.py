
n, p, k = map(int, input().split())
t = list(map(int, input().split()))

def calc_time(n, p, k, t):
    total_time = 0
    for i in range(n):
        total_time += (t[i] - total_time) * (100 + i * p) / 100
    total_time += (k - total_time) * (100 + n * p) / 100
    return total_time

def binary_search(n, p, k, t):
    lo = 0
    hi = k
    while lo < hi:
        mid = (lo + hi) // 2
        if calc_time(n, p, mid, t) < k:
            lo = mid + 1
        else:
            hi = mid
    return lo

print(binary_search(n, p, k, t))

