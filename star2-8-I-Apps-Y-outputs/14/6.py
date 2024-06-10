
X = int(input())
for i in range(X, 0, -1):
  for j in range(2, 100):
    if pow(i, j) <= X:
      print(pow(i, j))
      break
  else:
    continue
  break

