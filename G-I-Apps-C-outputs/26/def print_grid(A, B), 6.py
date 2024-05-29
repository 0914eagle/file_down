
def print_grid(A, B):
    h = max(2, A+1)
    w = max(2, B+1)
    
    grid = [['#' for _ in range(w)] for _ in range(h)]
    
    for i in range(1, h):
        for j in range(1, w):
            grid[i][j] = '.'
    
    print(h, w)
    for row in grid:
        print(''.join(row))

# Sample Input
A, B = map(int, input().split())

# Output the grid
print_grid(A, B)
