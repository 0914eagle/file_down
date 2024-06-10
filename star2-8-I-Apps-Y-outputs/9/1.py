
def water_spreading():
    N, M = map(int, input().split())
    grid = [list(input()) for _ in range(N)]
    
    def is_air(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        return grid[x][y] == '.'
    
    def is_water(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        return grid[x][y] == 'V'
    
    def is_stone(x, y):
        if x < 0 or x >= N or y < 0 or y >= M:
            return False
        return grid[x][y] == '#'
    
    def is_next_to_water(x, y):
        return is_water(x-1, y)
    
    def is_next_to_stone(x, y):
        return is_stone(x-1, y)
    
    def spread_water():
        for i in range(N):
            for j in range(M):
                if is_next_to_water(i, j) and is_air(i, j):
                    grid[i][j] = 'V'
        
        for i in range(N):
            for j in range(M):
                if is_next_to_water(i, j) and is_air(i, j-1):
                    grid[i][j-1] = 'V'
                if is_next_to_water(i, j) and is_air(i, j+1):
                    grid[i][j+1] = 'V'
    
    while True:
        changed = False
        for i in range(N):
            for j in range(M):
                if is_next_to_water(i, j) and is_air(i, j):
                    changed = True
        if not changed:
            break
        spread_water()
    
    for row in grid:
        print(''.join(row))

