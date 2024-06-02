
def solve(n, k, a):
    l = 1
    r = 10**9
    while l < r:
        m = (l + r) // 2
        cnt = 0
        for i in range(n):
            if a[i] <= m:
                cnt += 1
        if cnt < k:
            l = m + 1
        else:
            r = m
    if cnt < k:
        return -1
    else:
        return l

n, k = map(int, input().split())
a = list(map(int, input().split()))
print(solve(n, k, a))

