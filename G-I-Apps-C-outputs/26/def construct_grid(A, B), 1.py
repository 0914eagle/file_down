
def construct_grid(A, B):
    total_grid_size = A + B + 1
    grid = [['.' for _ in range(total_grid_size)] for _ in range(total_grid_size)]

    for i in range(A):
        grid[i][0] = '#'
    
    for i in range(A, total_grid_size):
        grid[i][total_grid_size - 1] = '#'

    grid[A][0] = '.'
    grid[A][total_grid_size - 1] = '#'

    print(total_grid_size, total_grid_size)
    for row in grid:
        print(''.join(row))

# Input
A, B = map(int, input().split())

# Call the function
construct_grid(A, B)
```
