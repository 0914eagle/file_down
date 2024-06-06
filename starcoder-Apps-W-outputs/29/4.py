
n, k = map(int, input().split())
a = list(map(int, input().split()))
ans = []

for i in range(n):
  x = min(k - 1, a[i])
  ans.append([j for j in range(1, x + 2)])
  for j in range(a[i] - x):
    ans[i].append(k)

for i in range(n):
  if len(ans[i]) != a[i]:
    print('NO')
    exit()

print('YES')
for i in range(n):
  print(' '.join(map(str, ans[i])))
