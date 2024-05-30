
def calculate_lipschitz_constant(points):
    points.sort()  # Sort the points based on x value
    
    lipschitz_constant = float('-inf')
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        
        slope = abs((y2 - y1) / (x2 - x1))
        lipschitz_constant = max(lipschitz_constant, slope)
    
    return lipschitz_constant

# Read input
N = int(input())
points = []
for _ in range(N):
    x, z = map(int, input().split())
    points.append((x, z))
    
print(calculate_lipschitz_constant(points))
```
