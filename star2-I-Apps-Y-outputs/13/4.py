
def solve(s):
  n = len(s)
  left = set()
  right = set()
  for i in range(n):
    left.add(s[i])
    right.add(s[n-i-1])
    if i >= n-i-1:
      continue
    common = left & right
    if len(common) == i+1:
      return i+1
  return 0

n = int(input())
s = input()
print(solve(s))

