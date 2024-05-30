
def find_lipschitz_constant(N, points):
    points.sort()  # Sort points based on x values
    lipschitz_constant = float('-inf')

    for i in range(1, N):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        slope = abs((y2 - y1) / (x2 - x1))
        lipschitz_constant = max(lipschitz_constant, slope)

    return lipschitz_constant

# Reading input
N = int(input())
points = []
for _ in range(N):
    x, z = map(int, input().split())
    points.append((x, z))

# Finding Lipschitz constant and printing the result
result = find_lipschitz_constant(N, points)
print(result)
```
