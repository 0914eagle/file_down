
def lipschitz_constant(N, points):
    points.sort(key=lambda x: x[0])  # Sort points based on x values
    max_slope = 0
    for i in range(1, N):
        slope = abs((points[i][1] - points[i-1][1]) / (points[i][0] - points[i-1][0]))
        max_slope = max(max_slope, slope)
    return max_slope

# Read input
N = int(input())
points = []
for _ in range(N):
    x, z = map(int, input().split())
    points.append((x, z))

# Calculate Lipschitz constant
result = lipschitz_constant(N, points)
print(result)
```
