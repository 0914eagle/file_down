
import math

def max_pickles(s, r, n, z):
    sandwich_area = math.pi * s**2
    pickle_area = math.pi * r**2
    max_pickles = min(n, math.floor(z/100 * sandwich_area / pickle_area))
    return max_pickles

# Input
s, r = map(float, input().split())
n, z = map(int, input().split())

# Output
print(max_pickles(s, r, n, z))
