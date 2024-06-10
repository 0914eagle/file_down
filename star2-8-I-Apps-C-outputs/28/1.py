
def solve(s):
  n = len(s)
  ans = 0
  for i in range(n):
    if s[i] == '0':
      ans = max(ans, i)
  return ans

if __name__ == "__main__":
  s = input()
  print(solve(s))

