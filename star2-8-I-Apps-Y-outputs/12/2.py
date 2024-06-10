
h, m = map(int, input().split())

if m >= 45:
  m = m - 45
  print(h, m)
else:
  m = m + 15
  h = h - 1
  if h < 0:
    h = 23
  print(h, m)

