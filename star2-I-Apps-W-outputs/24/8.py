
n = int(input())
a = list(map(int, input().split()))

def f(l, r):
    res = 0
    for i in range(l, r+1):
        if a[i-1] >= l and a[i-1] <= r:
            res += 1
    return res

ans = 0
for l in range(1, n+1):
    for r in range(l, n+1):
        ans += f(l, r)
print(ans)

