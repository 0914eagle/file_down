
def max_flowers_visited(N, R, C, field):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    
    def is_valid_move(r, c, new_r, new_c):
        if new_r < 0 or new_r >= N or new_c < 0 or new_c >= N:
            return False
        if abs(r - new_r) == 1 and abs(c - new_c) > 1:
            return True
        if abs(c - new_c) == 1 and abs(r - new_r) > 1:
            return True
        return False
    
    def dfs(r, c, prev_petals):
        visited[r][c] = 1
        max_flowers = 1
        
        for dr, dc in directions:
            new_r, new_c = r + dr, c + dc
            if is_valid_move(r, c, new_r, new_c) and not visited[new_r][new_c] and field[new_r][new_c] > prev_petals:
                max_flowers = max(max_flowers, 1 + dfs(new_r, new_c, field[new_r][new_c]))
        
        visited[r][c] = 0
        return max_flowers
    
    return dfs(R-1, C-1, field[R-1][C-1])

# Read input
N = int(input())
R, C = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# Calculate the largest number of flowers the grasshopper can visit
result = max_flowers_visited(N, R, C, field)
print(result)
