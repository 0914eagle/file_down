
a, b = map(int, input().split())

s = []
for i in range(a):
  s.append([])

for i in range(b):
  u, v = map(int, input().split())
  s[u - 1].append(v - 1)
  s[v - 1].append(u - 1)

flag = False
for i in range(1, a):
  for j in s[i]:
    if i in s[j]:
      flag = True
      break
  if flag:
    break

if flag:
  print("Yes")
else:
  print("No")
