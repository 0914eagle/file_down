
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def simulate_command(cmd):
        moves = {'L': (0, -1), 'R': (0, 1), 'U': (-1, 0), 'D': (1, 0)}
        return moves[cmd]

    def find_path(command):
        x, y = start
        changes = 0
        for cmd in command:
            dx, dy = simulate_command(cmd)
            new_x, new_y = x + dx, y + dy
            if is_valid_move(new_x, new_y):
                x, y = new_x, new_y
            else:
                changes += 1
        return changes

    for i in range(len(command)):
        for cmd in 'LRUD':
            new_command = command[:i] + cmd + command[i:]
            changes = find_path(new_command)
            if (x, y) == goal:
                return changes

    return find_path(command)

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
start = (0, 0)
goal = (0, 0)
for i in range(H):
    for j in range(W):
        if grid[i][j] == 'S':
            start = (i, j)
        elif grid[i][j] == 'G':
            goal = (i, j)
command = input()

# Call the function and output the result
print(fix_robot_command(grid, command))
