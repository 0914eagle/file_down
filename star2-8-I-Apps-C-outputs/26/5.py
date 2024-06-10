
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
p = sum(w)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)
for i in range(n):
    if a[i] == 0:
        w[i] -= m
    else:
        w[i] += m
    q = w[i]
    g = gcd(p, q)
    p //= g
    q //= g
    r = pow(q, 998244353 - 2, 998244353)
    print(q * r % 998244353)

