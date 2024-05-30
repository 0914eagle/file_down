
def find_lipschitz_constant(N, points):
    points = sorted(points, key=lambda x: x[0])
    lipschitz_constant = 0
    for i in range(1, len(points)):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        lipschitz_constant = max(lipschitz_constant, abs((y2 - y1) / (x2 - x1)))
    return lipschitz_constant

# Read input
N = int(input())
points = [tuple(map(float, input().split())) for _ in range(N)]

# Find Lipschitz constant
result = find_lipschitz_constant(N, points)
print(result)
```
