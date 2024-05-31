
def max_flowers(N, R, C, flowers):
    directions = [(-1, -2), (-1, 2), (1, -2), (1, 2), (-2, -1), (-2, 1), (2, -1), (2, 1)]

    def is_valid_move(x, y):
        return 0 <= x < N and 0 <= y < N

    def can_jump(prev_petals, next_petals):
        return next_petals > prev_petals

    def dfs(x, y, visited, prev_petals):
        max_flowers_visited = 1
        visited.add((x, y))

        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y) and (new_x, new_y) not in visited and can_jump(flowers[x][y], flowers[new_x][new_y]):
                max_flowers_visited = max(max_flowers_visited, 1 + dfs(new_x, new_y, visited, flowers[x][y]))

        visited.remove((x, y))
        return max_flowers_visited

    return dfs(R - 1, C - 1, set(), 0)

# Input parsing
N = int(input())
R, C = map(int, input().split())
flowers = [list(map(int, input().split())) for _ in range(N)]

result = max_flowers(N, R, C, flowers)
print(result)
