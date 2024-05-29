
def solve_grid(A, B):
    # Initialize grid with all black squares
    grid = [['#' for _ in range(100)] for _ in range(100)]

    # Paint white squares
    for i in range(A - 1):
        grid[i // 50 * 2][i % 50 * 2] = '.'
    
    # Paint black squares
    for i in range(B - 1):
        grid[50 + i // 50 * 2][i % 50 * 2] = '.'
    
    # Determine grid size
    h = 100 if A > 50 or B > 50 else 2
    w = 100 if A > 50 and B > 50 else 2

    # Print grid
    print(h, w)
    for row in grid[:h]:
        print(''.join(row[:w]))

# Take input
A, B = map(int, input().split())

solve_grid(A, B)
```
