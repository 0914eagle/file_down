
h, w = map(int, input().split())
r = list(map(int, input().split()))
c = list(map(int, input().split()))
MOD = 10**9 + 7

def ways(val, n):
    res = 1
    for i in range(n):
        res = (res * (val - i)) % MOD
    
    return res

res = 1
for i in range(h):
    res = (res * ways(r[i] + c[i], r[i])) % MOD

for j in range(w):
    res = (res * ways(r[j] + c[j], c[j])) % MOD

print(res)

