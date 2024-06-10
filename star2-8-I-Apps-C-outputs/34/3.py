
def solve(s):
  max_d = -1
  s = sorted(s)
  for i, a in enumerate(s):
    for j, b in enumerate(s[i + 1:], start=i + 1):
      for k, c in enumerate(s[j + 1:], start=j + 1):
        d = a + b + c
        if d in s:
          max_d = max(max_d, d)
  if max_d != -1:
    return max_d
  else:
    return 'no solution'

n = int(input())
s = set()
for i in range(n):
  s.add(int(input()))
print(solve(s))

