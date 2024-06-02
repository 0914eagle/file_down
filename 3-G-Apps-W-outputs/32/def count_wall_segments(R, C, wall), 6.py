
def count_wall_segments(R, C, wall):
    def dfs(row, col):
        if row < 0 or row >= R or col < 0 or col >= C or wall[row][col] != 'B':
            return
        wall[row][col] = '.'
        dfs(row+1, col)
        dfs(row-1, col)
        dfs(row, col+1)
        dfs(row, col-1)

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

# Call the function and print the output
print(count_wall_segments(R, C, wall))
