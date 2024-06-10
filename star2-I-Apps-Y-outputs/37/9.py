
n = int(input())
a = [int(input()) for _ in range(n)]

s = set()
for i in a:
  if i in s:
    s.remove(i)
  else:
    s.add(i)
print(len(s))

