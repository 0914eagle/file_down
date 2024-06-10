
import math

def solve(s, r, n, z):
  sandwich_area = math.pi * s**2
  pickle_area = math.pi * r**2
  max_pickle_area = sandwich_area * z / 100
  max_pickles = max_pickle_area / pickle_area
  return min(n, math.floor(max_pickles))

s, r, n, z = map(float, input().split())
n, z = map(int, input().split())
print(solve(s, r, n, z))

