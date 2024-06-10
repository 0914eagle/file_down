
for case in range(int(input())):
  n = int(input())
  a = [0] * n
  b = [0] * n
  c = [0] * n
  for i in range(n):
    a[i], b[i], c[i] = map(int, input().split())
  a.sort()
  b.sort()
  c.sort()
  res = 0
  i = 0
  j = 0
  k = 0
  while i < n and j < n and k < n:
    if a[i] <= b[j] and a[i] <= c[k]:
      res += 1
      i += 1
    elif b[j] <= a[i] and b[j] <= c[k]:
      res += 1
      j += 1
    elif c[k] <= a[i] and c[k] <= b[j]:
      res += 1
      k += 1
  print("Case #{}: {}".format(case+1, res))

