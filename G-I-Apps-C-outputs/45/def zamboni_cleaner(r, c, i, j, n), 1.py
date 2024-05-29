
def zamboni_cleaner(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    grid = [['.' for _ in range(c)] for _ in range(r)]
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    direction_index = 0
    color_index = 0
    step_size = 1
    
    current_row = i - 1
    current_col = j - 1
    
    for _ in range(n):
        for _ in range(step_size):
            if grid[current_row][current_col] == '.':
                grid[current_row][current_col] = colors[color_index]
            else:
                grid[current_row][current_col] = '.'
            current_row = (current_row + directions[direction_index][0]) % r
            current_col = (current_col + directions[direction_index][1]) % c
        
        direction_index = (direction_index + 1) % 4
        color_index = (color_index + 1) % 26
        step_size += 1
    
    grid[i-1][j-1] = '@'
    
    for row in grid:
        print(''.join(row))

# Input parsing
input_line = input().split()
r, c, i, j, n = map(int, input_line)

zamboni_cleaner(r, c, i, j, n)
```
