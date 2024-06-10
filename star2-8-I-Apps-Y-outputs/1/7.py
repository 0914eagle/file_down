
n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(set(a)) > k:
  print('NO')
else:
  print('YES')
  d = dict()
  for i in range(n):
    if a[i] not in d:
      d[a[i]] = i+1
  c = [0] * n
  for i in range(n):
    c[i] = d[a[i]]
  print(*c)

