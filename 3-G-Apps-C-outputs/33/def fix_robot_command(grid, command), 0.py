
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def simulate_command(command):
        x, y = start_pos
        for move in command:
            if move == 'L':
                y -= 1
            elif move == 'R':
                y += 1
            elif move == 'U':
                x -= 1
            elif move == 'D':
                x += 1

            if not is_valid_move(x, y):
                return False

            if grid[x][y] == 'G':
                return True

        return False

    changes_needed = float('inf')
    start_pos = (0, 0)
    goal_pos = (0, 0)

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'G':
                goal_pos = (i, j)

    for i in range(len(command) + 1):
        for move in ['L', 'R', 'U', 'D']:
            new_command = command[:i] + move + command[i:]
            if simulate_command(new_command):
                changes_needed = min(changes_needed, abs(i - len(command)))

    return changes_needed

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
command = input()

# Call the function and output the result
print(fix_robot_command(grid, command))
