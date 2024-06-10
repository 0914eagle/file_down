
n, m = map(int, input().split())
a = list(map(int, input().split()))
w = list(map(int, input().split()))

for i in range(n):
    w[i] = w[i] + a[i] - 1

q = [0] * n
for i in range(n):
    q[i] = w[i] * m

p = sum(q)
MOD = 998244353

def inv(x):
    return pow(x, MOD-2, MOD)

for i in range(n):
    r = q[i] * inv(p) % MOD
    print(r)

