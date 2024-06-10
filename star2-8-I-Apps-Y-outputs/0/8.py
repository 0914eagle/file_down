
t = int(input())
for _ in range(t):
  n = int(input())
  s = input()
  x, y = 0, 0
  for c in s:
    if c == 'L':
      x -= 1
    elif c == 'R':
      x += 1
    elif c == 'U':
      y += 1
    elif c == 'D':
      y -= 1
  if x == y == 0:
    print(-1)
  else:
    print(1, n)

