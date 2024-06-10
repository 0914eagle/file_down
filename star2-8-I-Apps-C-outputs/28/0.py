
def solve(s):
  n = len(s)
  time = 0
  for i in range(n):
    if s[i] == '1':
      time += 2 * (n - i)
  return time

