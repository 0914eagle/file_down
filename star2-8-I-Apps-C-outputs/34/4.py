
def solve(s):
  s = sorted(s)
  n = len(s)
  max_d = -1
  for i in range(n - 3):
    for j in range(i + 1, n - 2):
      for k in range(j + 1, n - 1):
        d = s[i] + s[j] + s[k]
        if d in s[k + 1:]:
          max_d = max(max_d, d)
  if max_d == -1:
    return "no solution"
  return str(max_d)

n = int(input())
s = set()
for i in range(n):
  s.add(int(input()))
print(solve(s))

