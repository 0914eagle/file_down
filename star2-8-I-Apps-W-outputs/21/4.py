
n = int(input())
p = list(map(int, input().split()))

def ncr(n, r):
    res = 1
    for i in range(min(r, n - r)):
        res = res * (n - i) // (i + 1)
    return res

def inverse(a):
    return pow(a, M - 2, M)

M = 998244353

def solve(n, p):
    res = 1
    for i in range(n):
        p_i = p[i]
        q_i = 100 - p_i
        a = p_i
        b = q_i
        c = 100
        res = (res * ncr(b, a) * pow(c, a, M)) % M
    return res

print(solve(n, p))

