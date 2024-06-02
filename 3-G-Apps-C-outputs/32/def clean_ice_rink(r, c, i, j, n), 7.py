
def clean_ice_rink(r, c, i, j, n):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    ice_rink[i-1][j-1] = '@'
    
    current_color = 'A'
    current_direction = 0
    step_size = 1
    
    for _ in range(n):
        for _ in range(step_size):
            i = (i + directions[current_direction][0]) % r
            j = (j + directions[current_direction][1]) % c
            
            if ice_rink[i][j] == '.':
                ice_rink[i][j] = current_color
            else:
                current_color = chr((ord(ice_rink[i][j]) - ord('A') + 1) % 26 + ord('A'))
                ice_rink[i][j] = current_color
        
        current_direction = (current_direction + 1) % 4
        step_size += 1
    
    for row in ice_rink:
        print(''.join(row))

# Input processing
input_data = input().strip().split()
r, c, i, j, n = map(int, input_data)

clean_ice_rink(r, c, i, j, n)
