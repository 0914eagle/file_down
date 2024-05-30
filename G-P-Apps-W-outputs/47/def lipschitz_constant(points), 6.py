
import sys

def lipschitz_constant(points):
    points.sort()
    n = len(points)
    max_slope = float('-inf')
    
    for i in range(1, n):
        slope = abs((points[i][1] - points[i-1][1]) / (points[i][0] - points[i-1][0]))
        max_slope = max(max_slope, slope)
    
    return max_slope

# Read input
lines = sys.stdin.readlines()
n = int(lines[0])
points = [tuple(map(int, line.strip().split())) for line in lines[1:]]

# Calculate Lipschitz constant
result = lipschitz_constant(points)
print(result)
```
