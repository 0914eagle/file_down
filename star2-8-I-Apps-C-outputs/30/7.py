

n, q = map(int, input().split())
operations = []
for _ in range(q):
  a, b = input().split()
  operations.append((a, b))

result = 0
for i in range(6):
  for j in range(6):
    s = chr(ord('a') + i) + chr(ord('a') + j)
    for _ in range(n-2):
      found = False
      for a, b in operations:
        if s[:2] == a:
          s = b + s[2:]
          found = True
          break
      if not found:
        break
    if s == 'a':
      result += 1

print(result)


