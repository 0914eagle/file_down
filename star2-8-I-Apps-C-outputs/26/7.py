
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))
l = 998244353
p = [0] * n
for i in range(n):
    if a[i] == 0:
        p[i] -= w[i]
    else:
        p[i] += w[i]
for i in range(n):
    p[i] = (p[i] + l) % l
for _ in range(m):
    sum_p = sum(p)
    q = [0] * n
    for i in range(n):
        q[i] = p[i] * n
        q[i] += l
        q[i] %= l
    p = q
for q in p:
    p, q = q, 1
    g = math.gcd(p, q)
    p //= g
    q //= g
    r = pow(p, l - 2, l)
    r = (r * q) % l
    print(r)

