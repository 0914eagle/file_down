
from math import pi

def solve(s, r, n, z):
    max_area = (z / 100) * pi * s ** 2
    pickle_area = pi * r ** 2
    num_pickles = max_area // pickle_area
    return int(num_pickles)

