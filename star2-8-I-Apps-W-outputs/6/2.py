
n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))

def nCr(n, r):
    if n < r:
        return 0
    if n == r or r == 0:
        return 1
    return nCr(n-1, r-1) + nCr(n-1, r)

def f(n, r):
    if n < r:
        return 0
    return nCr(n, r) * m**(n-r)

def g(n, r):
    if n < r:
        return 0
    return nCr(n, r) * m**n

a = s1.count(0)
b = s2.count(0)
l = min(a, b)
c = 0
for i in range(l+1):
    c += f(a, i) * f(b, i)
d = 1
for i in range(l+1):
    d *= g(a, i) * g(b, i)

def modinv(a, m):
    a = a % m
    for x in range(m):
        if a * x % m == 1:
            return x
    return 1

print((c * modinv(d, 10**9+7)) % (10**9+7))

