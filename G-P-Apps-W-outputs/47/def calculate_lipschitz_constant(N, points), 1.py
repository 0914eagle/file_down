
def calculate_lipschitz_constant(N, points):
    sorted_points = sorted(points, key=lambda x: x[0])
    max_diff = 0
    for i in range(1, N):
        diff = abs((sorted_points[i][1] - sorted_points[i-1][1]) / (sorted_points[i][0] - sorted_points[i-1][0]))
        max_diff = max(max_diff, diff)
    return max_diff

# Read input
N = int(input())
points = []
for _ in range(N):
    x, z = map(int, input().split())
    points.append((x, z))

# Calculate and print Lipschitz constant
print(calculate_lipschitz_constant(N, points))
```
