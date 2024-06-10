
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
prod = 1
for i in range(n-1):
  for j in range(i+1, n):
    prod *= abs(a[i] - a[j])
    prod %= m
print(prod)

