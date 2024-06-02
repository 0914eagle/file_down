
def min_moves_to_goal(maze):
    rows = len(maze)
    cols = len(maze[0])
    
    def is_valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def dfs(row, col, moves):
        if not is_valid_move(row, col) or maze[row][col] == '#':
            return
        if maze[row][col] == 'M':
            return
        if maze[row][col] == '.' or maze[row][col] == '_':
            if moves < maze[row][col]:
                maze[row][col] = moves
            else:
                return
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_row, new_col = row + dr, col + dc
            dfs(new_row, new_col, moves + 1)
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == 'M':
                dfs(i, j, 0)
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] == '.' or maze[i][j] == '_':
                maze[i][j] = -1
    
    return maze

# Input
C, R = map(int, input().split())
maze = []
for _ in range(R):
    maze.append(list(input().strip()))

# Compute minimum moves to goal
result = min_moves_to_goal(maze)

# Output
for row in result:
    print(' '.join(map(str, row)))
