
def lipschitz_constant(N, points):
    points.sort()
    lipschitz = 0
    for i in range(1, N):
        diff = abs(points[i][1] - points[i-1][1]) / abs(points[i][0] - points[i-1][0])
        lipschitz = max(lipschitz, diff)
    return lipschitz

# Input processing
N = int(input())
points = []
for _ in range(N):
    x, z = map(int, input().split())
    points.append((x, z))

# Call the function and print the result
print(lipschitz_constant(N, points))
```
