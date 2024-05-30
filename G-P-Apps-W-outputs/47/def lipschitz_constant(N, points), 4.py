
def lipschitz_constant(N, points):
    points.sort(key=lambda x: x[0])
    
    lipschitz = float('-inf')
    for i in range(1, N):
        x1, y1 = points[i-1]
        x2, y2 = points[i]
        slope = abs((y2 - y1) / (x2 - x1))
        lipschitz = max(lipschitz, slope)
    
    return lipschitz

# Reading input
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

# Calculating and printing Lipschitz constant
print(lipschitz_constant(N, points))
```
