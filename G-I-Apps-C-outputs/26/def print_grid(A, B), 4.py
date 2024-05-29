
def print_grid(A, B):
    grid = [['#' for _ in range(100)] for _ in range(100)]
    
    # Paint A connected components white
    for i in range(A-1):
        grid[i//50*2][i%50*2] = '.'
    
    # Paint B connected components black
    for i in range(B-1):
        grid[i//50*2][49 + i%50*2] = '.'

    # Determine grid size
    h = 100 if A > 50 else 2
    w = 100 if B > 50 else 2

    # Print grid
    print(h, w)
    for row in grid[:h]:
        print(''.join(row[:w]))

# Input
A, B = map(int, input().split())

# Output
print_grid(A, B)
```
