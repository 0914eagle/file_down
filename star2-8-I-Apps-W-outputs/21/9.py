
n = int(input())
p = list(map(int, input().split()))
def expo(x, y, m):
    res = 1
    x = x % m
    while (y > 0):
        if (y & 1):
            res = (res*x) % m
        y = y>>1
        x = (x*x) % m
    return res
def modinv(a, m):
    return expo(a, m-2, m)
m = 998244353
ans = 0
for i in range(n):
    temp = p[i] * modinv(100, m)
    temp = (temp * (m + 1 - temp)) % m
    ans = (ans + temp) % m
print(ans)

