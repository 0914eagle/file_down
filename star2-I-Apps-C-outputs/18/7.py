
import math

def solve(s, r, n, z):
  area_sandwich = math.pi * s**2
  area_pickle = math.pi * r**2
  max_area = area_sandwich * z / 100
  max_pickles = max_area / area_pickle
  return min(n, math.floor(max_pickles))

s, r, n, z = map(float, input().split())
n, z = map(int, input().split())
print(solve(s, r, n, z))

