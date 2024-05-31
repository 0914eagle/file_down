
def max_flowers_visited(N, R, C, field):
    directions = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

    def dfs(row, col, prev_petals, visited):
        visited.add((row, col))
        max_visited = 1

        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc

            if 0 <= new_row < N and 0 <= new_col < N and (new_row, new_col) not in visited and field[new_row][new_col] > prev_petals:
                max_visited = max(max_visited, 1 + dfs(new_row, new_col, field[new_row][new_col], visited.copy()))

        return max_visited

    return dfs(R - 1, C - 1, field[R - 1][C - 1], set())

# Read input
N = int(input())
R, C = map(int, input().split())
field = [list(map(int, input().split())) for _ in range(N)]

# Calculate and print the result
print(max_flowers_visited(N, R, C, field))
