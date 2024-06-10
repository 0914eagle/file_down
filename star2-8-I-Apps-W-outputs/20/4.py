
n, m = map(int, input().split())
a = list(map(int, input().split()))

ans = 1
for i in range(n):
  for j in range(i+1, n):
    ans = (ans * abs(a[i] - a[j])) % m

print(ans)

