
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
ans = [0] * n
for i in range(n):
    if a[i]:
        ans[i] = w[i] + m
    else:
        ans[i] = w[i] - m
mod = 998244353
for i in range(n):
    g = math.gcd(ans[i], mod)
    ans[i] //= g
    mod //= g
    print(ans[i])

