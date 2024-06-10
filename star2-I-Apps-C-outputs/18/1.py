
from math import pi

def solve(s, r, n, z):
    max_area = s**2 * pi
    max_pickle_area = max_area * z / 100
    pickle_area = r**2 * pi
    return min(n, int(max_pickle_area / pickle_area))

s, r, n, z = map(float, input().split())
print(solve(s, r, n, z))

