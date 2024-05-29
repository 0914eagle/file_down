
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    ice_rink = [['.'] * c for _ in range(r)]
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    color_index = 0
    
    row, col = i - 1, j - 1  # Convert 1-indexed to 0-indexed
    
    for step in range(1, n + 1):
        direction = directions[(step - 1) % 4]
        
        for _ in range(step):
            ice_rink[row][col] = colors[color_index]
            row = (row + direction[0]) % r
            col = (col + direction[1]) % c
        
        color_index = (color_index + 1) % 26
    
    ice_rink[i-1][j-1] = '@'
    
    for row in ice_rink:
        print(''.join(row))

# Input
input_str = input().strip()
r, c, i, j, n = map(int, input_str.split())

# Output
clean_ice_rink(r, c, i, j, n)
```
