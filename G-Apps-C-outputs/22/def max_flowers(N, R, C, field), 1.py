
def max_flowers(N, R, C, field):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    def valid_move(r1, c1, r2, c2):
        if abs(r1 - r2) == 1 and abs(c1 - c2) > 1:
            return True
        if abs(c1 - c2) == 1 and abs(r1 - r2) > 1:
            return True
        return False
    
    def dfs(r, c, petals, visited):
        visited[r][c] = True
        max_flowers = 1
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and field[nr][nc] > petals:
                max_flowers = max(max_flowers, 1 + dfs(nr, nc, field[nr][nc], visited))
        visited[r][c] = False
        return max_flowers
    
    visited = [[False for _ in range(N)] for _ in range(N)]
    return dfs(R-1, C-1, field[R-1][C-1], visited)

# Read input
N = int(input())
R, C = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(max_flowers(N, R, C, field))
