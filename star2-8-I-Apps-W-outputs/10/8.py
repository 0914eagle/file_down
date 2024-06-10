
n = int(input())
a = list(map(int, input().split()))
a.sort()

def solve(a):
  s = 0
  i = 0
  j = len(a) - 1
  res = 360
  while i <= j:
    s += a[i]
    res = min(res, abs(s - (360 - s)))
    if s > 180:
      s -= a[i]
      i += 1
    elif s < 180:
      s -= a[j]
      j -= 1
    else:
      break
  return res

print(solve(a))

