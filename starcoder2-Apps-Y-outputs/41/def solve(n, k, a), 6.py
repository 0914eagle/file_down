
def solve(n, k, a):
    l, r = 1, 10**9
    while l < r:
        m = (l + r) // 2
        if sum(x <= m for x in a) >= k:
            r = m
        else:
            l = m + 1
    return l if sum(x <= l for x in a) == k else -1

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

