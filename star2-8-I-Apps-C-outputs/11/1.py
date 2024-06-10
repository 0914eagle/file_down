
def ice_rink(r, c, i, j, n):
    grid = [['.'] * c for _ in range(r)]
    direction = 0 # 0: up, 1: right, 2: down, 3: left
    colors = [chr(x) for x in range(ord('A'), ord('Z')+1)]
    cur_color = 0
    x, y = i-1, j-1
    for _ in range(n):
        grid[x][y] = colors[cur_color]
        if direction == 0: # up
            x = (x-1) % r
        elif direction == 1: # right
            y = (y+1) % c
        elif direction == 2: # down
            x = (x+1) % r
        elif direction == 3: # left
            y = (y-1) % c
        direction = (direction+1) % 4
        cur_color = (cur_color+1) % len(colors)
    grid[x][y] = '@'
    return grid

if __name__ == '__main__':
    r, c, i, j, n = map(int, input().split())
    grid = ice_rink(r, c, i, j, n)
    for row in grid:
        print(''.join(row))

