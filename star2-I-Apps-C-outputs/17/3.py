
def solve(s):
  n = len(s)
  if n == 1:
    return 0
  if n % 2 == 0:
    mid = n // 2
  else:
    mid = n // 2 + 1
  steps = 0
  for i in range(mid):
    if s[i] != s[n - i - 1]:
      steps += min(abs(ord(s[i]) - ord(s[n - i - 1])), 10 - abs(ord(s[i]) - ord(s[n - i - 1])))
  return steps

s = input()
print(solve(s))

