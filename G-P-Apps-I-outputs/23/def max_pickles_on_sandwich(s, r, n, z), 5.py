
import math

def max_pickles_on_sandwich(s, r, n, z):
    def calc_area(r):
        return math.pi * r**2
    
    def can_fit_pickles(s, r, n, z):
        total_area = math.pi * s**2
        max_pickles_area = total_area * z / 100
        pickle_area = calc_area(r) * n
        return pickle_area <= max_pickles_area
    
    def max_pickles(s, r):
        return int(math.pi * s**2 / calc_area(r))
    
    while not can_fit_pickles(s, r, n, z):
        r -= 0.000001
    
    return max_pickles(s, r)

# Sample Input
s, r = map(float, input().split())
n, z = map(int, input().split())

result = max_pickles_on_sandwich(s, r, n, z)
print(result)
```
