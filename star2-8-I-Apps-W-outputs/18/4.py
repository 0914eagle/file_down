
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]
res = 0
while any(h):
  m = h.index(max(h))
  h[m] -= a
  for i in range(n):
    if i != m:
      h[i] -= b
  res += 1
print(res)

