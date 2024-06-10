
A, B = map(int, input().split())
for x in range(1, 10001):
  if (x * 8 // 100 == A and x * 10 // 100 == B) or (x * 8 // 100 == B and x * 10 // 100 == A):
    print(x)
    break
else:
  print(-1)

