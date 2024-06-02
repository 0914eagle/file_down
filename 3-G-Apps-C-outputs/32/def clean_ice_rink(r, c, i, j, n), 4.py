
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i-1][j-1] = '@'
    
    current_color = 0
    current_direction = 3  # up
    step_size = 1
    
    for _ in range(n):
        for _ in range(step_size):
            i = (i + directions[current_direction][0]) % r
            j = (j + directions[current_direction][1]) % c
            ice_rink[i][j] = colors[current_color]
        
        current_direction = (current_direction + 1) % 4
        current_color = (current_color + 1) % 26
        step_size += 1
    
    for row in ice_rink:
        print(''.join(row))

# Input parsing
input_values = input().split()
r, c, i, j, n = map(int, input_values)
clean_ice_rink(r, c, i, j, n)
