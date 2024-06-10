
import sys

def solve(n):
  a = [0] * (n + 1)
  a[-1] = 1
  b = [0] * (n + 1)
  b[-2] = 1
  return a, b

n = int(sys.stdin.readline())
a, b = solve(n)
print(len(a) - 1)
print(' '.join(map(str, a)))
print(len(b) - 1)
print(' '.join(map(str, b)))

