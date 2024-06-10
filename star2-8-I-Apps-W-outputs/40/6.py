
n, m = map(int, input().split())
a = [[] for i in range(n+1)]
b = [[] for i in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  a[x].append(y)
  b[y].append(x)
for i in range(1, n+1):
  if len(a[i]) == n-1 or len(b[i]) == n-1:
    print("YES")
    break
else:
  print("NO")

