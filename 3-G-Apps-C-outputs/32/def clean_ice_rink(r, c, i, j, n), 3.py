
def clean_ice_rink(r, c, i, j, n):
    colors = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    current_dir = 3  # start facing up
    current_color = 0
    
    steps = 1
    steps_taken = 0
    x, y = i-1, j-1
    
    while steps_taken < n:
        for _ in range(steps):
            if 0 <= x < r and 0 <= y < c:
                ice_rink[x][y] = colors[current_color]
            x += directions[current_dir][0]
            y += directions[current_dir][1]
            steps_taken += 1
        
        current_dir = (current_dir + 1) % 4
        current_color = (current_color + 1) % 26
        steps += 1
    
    ice_rink[x-directions[current_dir][0]][y-directions[current_dir][1]] = '@'
    
    for row in ice_rink:
        print(''.join(row))

# Input parsing
input_values = input().split()
r, c, i, j, n = map(int, input_values)
clean_ice_rink(r, c, i, j, n)
