
# 풀이
n, m = map(int, input().split())
black = []
for _ in range(m):
  black.append(list(map(int, input().split())))

for i in range(m):
  temp = []
  for j in range(m):
    if i == j:
      continue
    else:
      a, b, c, d = black[i]
      e, f, g, h = black[j]
      if a <= e <= c and b <= f <= d:
        continue
      elif a <= g <= c and b <= h <= d:
        continue
      elif e <= a <= g and f <= b <= h:
        continue
      elif e <= c <= g and f <= d <= h:
        continue
      elif a <= e <= c and b <= h <= d:
        continue
      elif a <= g <= c and b <= f <= d:
        continue
      elif e <= a <= g and f <= d <= h:
        continue
      elif e <= c <= g and f <= b <= h:
        continue
      else:
        temp.append(j)
  for k in temp:
    black[k][0] = black[k][2]
    black[k][1] = black[k][3]

# print(black)

temp = []
for i in range(m):
  a, b, c, d = black[i]
  if a > b:
    black[i][1] = a
    black[i][0] = b
  if c > d:
    black[i][3] = c
    black[i][2] = d
  temp.append(black[i])

# print(temp)
result = 0
for i in range(m):
  a, b, c, d = temp[i]
  result += (c-a) * (d-b)

print(result)

