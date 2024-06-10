
def solve(s):
  n = len(s)
  l = [1 if c == '1' else 0 for c in s]
  d = {}
  for i in range(n):
    if l[i]:
      for j in range(i, n):
        d[(i, j)] = 1
  ans = 0
  for i in range(n):
    if l[i] == 0:
      ans += 1
  return ans

if __name__ == '__main__':
  s = input()
  print(solve(s))

