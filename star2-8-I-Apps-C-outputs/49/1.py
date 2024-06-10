
n, l = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

def potato_price(a, c, l):
  s = sum(a)
  p1 = p2 = 0
  for i in range(n):
    if l <= a[i]:
      p1 += c[i]
      a[i] -= l
      break
  p1 /= (s - l)
  p2 = c[i] / a[i]
  return p1 * p2

print(format(min(potato_price(a, c, l), potato_price(a, c, l + 1)), '.3f'))

