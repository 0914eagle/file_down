
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i-1][j-1] = '@'
    
    current_color_idx = 0
    current_direction = 3  # up
    step_size = 1
    
    for _ in range(n):
        for _ in range(step_size):
            i = (i + directions[current_direction][0]) % r
            j = (j + directions[current_direction][1]) % c
            if ice_rink[i][j] == '.':
                ice_rink[i][j] = colors[current_color_idx]
            else:
                ice_rink[i][j] = '.'
        
        current_direction = (current_direction + 1) % 4
        current_color_idx = (current_color_idx + 1) % 26
        step_size += 1
    
    for row in ice_rink:
        print(''.join(row))

# Input
r, c, i, j, n = map(int, input().split())
clean_ice_rink(r, c, i, j, n)
