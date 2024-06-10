
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
p = sum(w)

for i in range(n):
    if a[i] == 0:
        w[i] *= -1

for i in range(n):
    q = w[i] * m
    g = gcd(p, q)
    p //= g
    q //= g
    r = pow(q, -1, 998244353)
    print(q * r % 998244353)

