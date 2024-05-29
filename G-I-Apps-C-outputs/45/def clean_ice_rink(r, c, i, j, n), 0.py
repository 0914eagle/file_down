
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i-1][j-1] = '@'  # Initial position of the zamboni
    
    direction_idx = 3  # Zamboni starts facing up
    step_size = 1
    color_idx = 0
    
    for _ in range(1, n+1):
        for _ in range(step_size):
            i += directions[direction_idx][0]
            j += directions[direction_idx][1]
            
            if i == r + 1:
                i = 1
            elif i == 0:
                i = r
                
            if j == c + 1:
                j = 1
            elif j == 0:
                j = c
            
            if ice_rink[i-1][j-1] == '.':
                ice_rink[i-1][j-1] = colors[color_idx]
            else:
                ice_rink[i-1][j-1] = colors[(colors.index(ice_rink[i-1][j-1]) + 1) % len(colors)]
        
        direction_idx = (direction_idx + 1) % 4
        step_size += 1
        color_idx = (color_idx + 1) % len(colors)
    
    for row in ice_rink:
        print(''.join(row))

# Sample Input:
# 5 5 3 3 4
# Sample Output:
# .....
# ..BBC
# ..A.C
# ....C
# @DDDD

clean_ice_rink(5, 5, 3, 3, 4)
