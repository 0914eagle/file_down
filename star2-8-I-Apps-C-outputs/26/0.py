
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
p = sum(w)
def C(n, m):
    if m > n:
        return 0
    res = 1
    for i in range(m):
        res = res * (n - i) // (i + 1)
    return res
def solve(w, p):
    res = 0
    for i in range(len(w)):
        res += C(w[i], 1) * p // w[i]
    return res
for i in range(len(a)):
    if a[i] == 0:
        w[i] -= m
    else:
        w[i] += m
    p += m
res = solve(w, p)
print(res % 998244353)

