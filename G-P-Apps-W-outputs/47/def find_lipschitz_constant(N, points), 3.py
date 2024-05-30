
def find_lipschitz_constant(N, points):
    sorted_points = sorted(points)
    
    lipschitz_constant = float("-inf")
    for i in range(1, N):
        x1, z1 = sorted_points[i-1]
        x2, z2 = sorted_points[i]
        
        current_lipschitz = abs((z2 - z1) / (x2 - x1))
        lipschitz_constant = max(lipschitz_constant, current_lipschitz)
    
    return lipschitz_constant

# Reading input
N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

# Call the function and print the result
print(find_lipschitz_constant(N, points))
```
