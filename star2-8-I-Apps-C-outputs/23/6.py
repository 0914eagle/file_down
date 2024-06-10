
n, k1, k2 = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
for i in range(k1):
    a[i] += 1
for i in range(k2):
    b[i] += 1
err = 0
for i in range(n):
    err += (a[i] - b[i])**2
print(err)

