
n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
  if a == 0:
    return b
  return gcd(b % a, a)

g = a[0]
for i in range(1, n):
  g = gcd(g, a[i])
if g == 1:
  print(-1)
else:
  print(sum(a))

