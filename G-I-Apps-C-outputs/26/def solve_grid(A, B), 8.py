
def solve_grid(A, B):
    h = 3
    w = 3
    grid = [['#' for _ in range(w)] for _ in range(h)]

    for i in range(1, h):
        for j in range(1, w):
            if A > 1:
                grid[i][j] = '.'
                A -= 1
    
    for i in range(1, h):
        for j in range(1, w):
            if B > 1:
                grid[i][j] = '#'
                B -= 1
    
    print(f"{h} {w}")
    for row in grid:
        print("".join(row))

# Read input
A, B = map(int, input().split())

# Call the function
solve_grid(A, B)
```
