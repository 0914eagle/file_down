
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def dfs(x, y, idx):
        if idx == len(command):
            return 0

        changes = float('inf')
        dx, dy = 0, 0
        if command[idx] == 'L':
            dy = -1
        elif command[idx] == 'R':
            dy = 1
        elif command[idx] == 'U':
            dx = -1
        elif command[idx] == 'D':
            dx = 1

        if is_valid_move(x + dx, y + dy):
            changes = min(changes, dfs(x + dx, y + dy, idx + 1))
        changes = min(changes, 1 + dfs(x, y, idx + 1))

        return changes

    start_x, start_y = None, None
    goal_x, goal_y = None, None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start_x, start_y = i, j
            elif grid[i][j] == 'G':
                goal_x, goal_y = i, j

    return dfs(start_x, start_y, 0)

# Reading input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
command = input().strip()

# Calling the function and printing the output
print(fix_robot_command(grid, command))
