
import sys
def zamboni_clean(r, c, i, j, n):
    grid = [['.' for _ in range(c)] for _ in range(r)]
    color = 'A'
    current_i = i-1
    current_j = j-1
    direction = 0 # 0 -> right, 1 -> down, 2 -> left, 3 -> up
    for step in range(n):
        step_size = (step+1) % 26
        if direction == 0:
            current_j += step_size
            if current_j >= c:
                current_j -= c
        elif direction == 1:
            current_i += step_size
            if current_i >= r:
                current_i -= r
        elif direction == 2:
            current_j -= step_size
            if current_j < 0:
                current_j += c
        else:
            current_i -= step_size
            if current_i < 0:
                current_i += r
        if color == 'Z':
            color = 'A'
        else:
            color = chr(ord(color)+1)
        grid[current_i][current_j] = color
        direction = (direction+1) % 4
    
    for row in grid:
        print(''.join(row))
    
    print('@' + grid[i-1][j-1])

input_str = sys.stdin.read()
r, c, i, j, n = map(int, input_str.split())
zamboni_clean(r, c, i, j, n)

