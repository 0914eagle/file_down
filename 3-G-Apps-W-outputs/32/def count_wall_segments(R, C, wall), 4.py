
def count_wall_segments(R, C, wall):
    def dfs(r, c):
        if r < 0 or r >= R or c < 0 or c >= C or wall[r][c] == '.':
            return
        wall[r][c] = '.'
        dfs(r+1, c)
        dfs(r-1, c)
        dfs(r, c+1)
        dfs(r, c-1)
    
    segments = 0
    for r in range(R):
        for c in range(C):
            if wall[r][c] == 'B':
                segments += 1
                dfs(r, c)
    
    return segments

# Read input
R, C = map(int, input().split())
wall = [list(input().strip()) for _ in range(R)]

# Call the function and output the result
print(count_wall_segments(R, C, wall))
