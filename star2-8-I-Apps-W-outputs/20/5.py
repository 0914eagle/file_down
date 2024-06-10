
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
res = 1
for i in range(n-1):
    for j in range(i+1, n):
        res = (res * abs(a[i] - a[j])) % m
print(res)

