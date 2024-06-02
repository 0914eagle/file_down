
def min_moves_to_goal(C, R, maze):
    def valid_move(x, y):
        return 0 <= x < R and 0 <= y < C

    def bfs(start_x, start_y):
        queue = [(start_x, start_y, 0)]
        visited = set()
        while queue:
            x, y, moves = queue.pop(0)
            if maze[x][y] == 'M':
                return moves
            if (x, y) in visited:
                continue
            visited.add((x, y))

            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = x + dx, y + dy
                if valid_move(new_x, new_y) and maze[new_x][new_y] != '#':
                    queue.append((new_x, new_y, moves + 1))
        return -1

    result = []
    for i in range(R):
        row_result = []
        for j in range(C):
            if maze[i][j] == '#':
                row_result.append(-1)
            else:
                row_result.append(bfs(i, j))
        result.append(row_result)

    return result

# Input parsing
C, R = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(list(input().strip()))

# Compute minimum moves to goal for each square in the maze
output = min_moves_to_goal(C, R, maze)

# Output the result
for row in output:
    print(' '.join(map(str, row)))
