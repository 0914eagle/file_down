
n, m = map(int, input().split())
s1 = list(map(int, input().split()))
s2 = list(map(int, input().split()))
p = 1
q = 1
for i in range(n):
    if s1[i] == 0 and s2[i] == 0:
        p *= m
        q *= m
    elif s1[i] == 0:
        p *= 1
        q *= m
    elif s2[i] == 0:
        p *= (m - 1)
        q *= m
    else:
        if s1[i] > s2[i]:
            p *= 1
            q *= 1
        else:
            p *= 0
            q *= 1

mod = 10**9 + 7
def inverse(a, m):
    a = a % m
    for x in range(m):
        if (a * x) % m == 1:
            return x
    return 1

print((p * inverse(q, mod)) % mod)

