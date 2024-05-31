
def max_flowers(N, R, C, flowers):
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    def is_valid(r, c, next_r, next_c):
        return abs(r - next_r) == 1 and abs(c - next_c) > 1 or abs(c - next_c) == 1 and abs(r - next_r) > 1

    def can_jump(r, c, next_r, next_c):
        return 0 <= next_r < N and 0 <= next_c < N and not visited[next_r][next_c] and flowers[next_r][next_c] > flowers[r][c]

    def dfs(r, c):
        visited[r][c] = True
        max_flowers_visited = 1

        for dr, dc in directions:
            next_r, next_c = r + dr, c + dc
            if can_jump(r, c, next_r, next_c):
                max_flowers_visited = max(max_flowers_visited, 1 + dfs(next_r, next_c))

        visited[r][c] = False
        return max_flowers_visited

    return dfs(R-1, C-1)

# Read input
N = int(input())
R, C = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
result = max_flowers(N, R, C, flowers)
print(result)
