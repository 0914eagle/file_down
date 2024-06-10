
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

count = 0

for x in a:
  for y in b:
    if (x + y) % 2 == 1:
      count += 1
      b.remove(y)
      break

print(count)

