
import sys
import math

def slice_thickness(n, s, holes):
    total_volume = 100 * 100 * 100 * s
    hole_volume = sum(math.pi * r**2 for r, _, _, _ in holes)
    available_volume = total_volume - hole_volume
    slice_volume = available_volume / s
    slice_thickness = slice_volume / (100 * 100)
    return slice_thickness

if __name__ == "__main__":
    n, s = map(int, input().split())
    holes = []
    for _ in range(n):
        r, x, y, z = map(int, input().split())
        holes.append((r, x, y, z))
    
    result = slice_thickness(n, s, holes)
    for _ in range(s):
        print('{:.9f}'.format(result))
```
