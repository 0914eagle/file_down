
from sys import stdin
from collections import deque

def solve(n, f, h):
  hired = deque()
  fired = deque()
  f[0] = 0
  hired.append(f[0])
  for i in range(1, n):
    f[i] = min(f[i], hired[-1])
    while hired and f[i]:
      fired.append(hired.pop())
      f[i] -= 1
    hired.append(h[i])
    if hired:
      fired.append(hired.popleft())
  return fired

n = int(stdin.readline())
f = [0] * n
h = [0] * n
for i in range(n):
  f[i], h[i] = map(int, stdin.readline().split())

print(len(solve(n, f, h)))
print(" ".join(map(str, solve(n, f, h))))

