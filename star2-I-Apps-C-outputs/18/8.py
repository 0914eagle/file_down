
import math

def solve(s, r, n, z):
    sandwich_area = math.pi * s * s
    pickle_area = math.pi * r * r
    max_pickle_area = sandwich_area * z / 100
    max_pickle_count = int(max_pickle_area / pickle_area)
    return min(n, max_pickle_count)

s, r, n, z = map(float, input().split())
n = int(n)
z = int(z)
print(solve(s, r, n, z))

