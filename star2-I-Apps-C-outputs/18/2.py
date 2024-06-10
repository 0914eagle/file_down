
import math

def solve(s, r, n, z):
    area_sandwich = math.pi * s * s
    area_pickle = math.pi * r * r
    max_area_pickle = area_sandwich * z / 100
    max_pickle = max_area_pickle / area_pickle
    return min(n, math.floor(max_pickle))

s, r, n, z = map(float, input().split())
n, z = map(int, input().split())
print(solve(s, r, n, z))

