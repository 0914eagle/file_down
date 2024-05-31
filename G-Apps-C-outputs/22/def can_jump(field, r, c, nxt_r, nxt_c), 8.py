
def can_jump(field, r, c, nxt_r, nxt_c):
    if abs(r - nxt_r) == 1 and abs(c - nxt_c) > 1:
        return field[nxt_r][nxt_c] > field[r][c]
    if abs(c - nxt_c) == 1 and abs(r - nxt_r) > 1:
        return field[nxt_r][nxt_c] > field[r][c]
    return False

def dfs(field, visited, r, c):
    visited[r][c] = True
    max_path = 1
    for dr, dc in [(2, 0), (-2, 0), (0, 2), (0, -2)]:
        nxt_r, nxt_c = r + dr, c + dc
        if 0 <= nxt_r < len(field) and 0 <= nxt_c < len(field) and not visited[nxt_r][nxt_c] and field[nxt_r][nxt_c] > field[r][c]:
            max_path = max(max_path, 1 + dfs(field, visited, nxt_r, nxt_c))
    visited[r][c] = False
    return max_path

def largest_number_of_flowers(N, R, C, flowers):
    field = [list(row) for row in flowers]
    visited = [[False] * N for _ in range(N)]
    return dfs(field, visited, R - 1, C - 1)

# Input parsing
N = int(input())
R, C = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(N)]

# Output
print(largest_number_of_flowers(N, R, C, flowers))
