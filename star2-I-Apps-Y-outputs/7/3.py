
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = [int(input()) for _ in range(q)]

def solve(a, b):
  a.sort()
  res = []
  for target in b:
    i = 0
    count = 0
    while i < len(a) and target > 0:
      if target >= a[i]:
        target -= a[i]
        count += 1
      else:
        i += 1
    if target > 0:
      res.append(-1)
    else:
      res.append(count)
  return res

for ans in solve(a, b):
  print(ans)

