
def count_wall_segments(R, C, wall):
    def dfs(r, c):
        if r < 0 or r >= R or c < 0 or c >= C or visited[r][c] or wall[r][c] == '.':
            return
        visited[r][c] = True
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            dfs(r + dr, c + dc)

    visited = [[False for _ in range(C)] for _ in range(R)]
    segments = 0
    for r in range(R):
        for c in range(C):
            if not visited[r][c] and wall[r][c] == 'B':
                dfs(r, c)
                segments += 1
    return segments

# Input parsing
R, C = map(int, input().split())
wall = [input() for _ in range(R)]

# Call the function and print the output
print(count_wall_segments(R, C, wall))
