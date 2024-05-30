
def max_points(N, E, S_X, S_Y, C, cans):
    grid = [[0 for _ in range(N)] for _ in range(N)]
    energy = E
    points = 0
    
    for t in range(1, 101):
        for x, y, ct in cans:
            if ct == t and grid[x][y] == 0:
                if x == S_X and y == S_Y:
                    points += 1
                elif abs(x - S_X) + abs(y - S_Y) <= 1:
                    energy += 1
                else:
                    energy -= 1
                grid[x][y] = 1
                
        if energy <= 0:
            break
            
    return points

# Read input
N, E, S_X, S_Y, C = map(int, input().split())
cans = [list(map(int, input().split())) for _ in range(C)]

# Call the function and output the result
print(max_points(N, E, S_X, S_Y, C, cans))
```
