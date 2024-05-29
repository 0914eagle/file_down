
def clean_ice_rink(r, c, i, j, n):
    ice_rink = [['.' for _ in range(c)] for _ in range(r)]
    
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    current_dir = 3  # start facing up
    colors = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    color_index = 0
    steps = 1
    
    for step in range(n):
        for _ in range(steps):
            ice_rink[i-1][j-1] = colors[color_index]
            if step == n - 1:
                ice_rink[i-1][j-1] = '@'
            i = (i + directions[current_dir][0] + r - 1) % r + 1
            j = (j + directions[current_dir][1] + c - 1) % c + 1
        current_dir = (current_dir + 1) % 4
        color_index = (color_index + 1) % 26
        steps += 1
    
    for row in ice_rink:
        print(''.join(row))


# Input processing
test_input = input().split()
r, c, i, j, n = map(int, test_input)

# Call the function with the input values
clean_ice_rink(r, c, i, j, n)
```
