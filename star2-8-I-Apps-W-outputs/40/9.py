
n, m = map(int, input().split())
a = [set() for i in range(n+1)]
b = [set() for i in range(n+1)]
for i in range(m):
  x, y = map(int, input().split())
  a[x].add(y)
  b[y].add(x)
for i in range(1, n+1):
  if len(a[i]) == n-1 or len(b[i]) == n-1:
    print("YES")
    exit()
print("NO")

