
def solve(s):
  n = len(s)
  left = set()
  right = set()
  for i in range(n // 2):
    left.add(s[i])
  for i in range(n // 2, n):
    right.add(s[i])
  return len(left & right)

n = int(input())
s = input()
print(solve(s))

