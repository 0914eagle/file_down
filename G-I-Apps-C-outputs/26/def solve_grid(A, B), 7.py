
def solve_grid(A, B):
    h = max(A, B) + 1
    w = A * B + max(A, B) - 1

    grid = [['#' for _ in range(w)] for _ in range(h)]
    
    for i in range(1, A):
        grid[i][0] = '.'
    
    for j in range(A, w):
        grid[0][j] = '.'

    print(h, w)
    
    for row in grid:
        print(''.join(row))

# Input
A, B = map(int, input().split())

# Output
solve_grid(A, B)
```
