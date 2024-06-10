
import math
def solve(s, k):
  n = len(s)
  min_change = n
  for i in range(n - k + 1):
    change = 0
    for j in range(k):
      if s[i + j] != 'R' and j % 3 == 0:
        change += 1
      if s[i + j] != 'G' and j % 3 == 1:
        change += 1
      if s[i + j] != 'B' and j % 3 == 2:
        change += 1
    min_change = min(min_change, change)
  return min_change
q = int(input())
for i in range(q):
  n, k = map(int, input().split())
  s = input()
  print(solve(s, k))

