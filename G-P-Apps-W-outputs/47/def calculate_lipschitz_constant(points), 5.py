
import sys

def calculate_lipschitz_constant(points):
    points.sort(key=lambda x: x[0])
    
    lipschitz_constant = 0
    for i in range(1, len(points)):
        x1, y1 = points[i - 1]
        x2, y2 = points[i]
        
        current_lipschitz = abs((y2 - y1) / (x2 - x1))
        lipschitz_constant = max(lipschitz_constant, current_lipschitz)
    
    return lipschitz_constant

if __name__ == "__main__":
    n = int(input())
    points = [list(map(float, input().split())) for _ in range(n)]

    result = calculate_lipschitz_constant(points)
    print(result)
```
