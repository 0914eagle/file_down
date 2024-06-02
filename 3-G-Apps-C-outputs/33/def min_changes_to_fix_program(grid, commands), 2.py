
def min_changes_to_fix_program(grid, commands):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def simulate_path(commands):
        x, y = start_pos
        for command in commands:
            if command == 'L':
                y -= 1
            elif command == 'R':
                y += 1
            elif command == 'U':
                x -= 1
            elif command == 'D':
                x += 1

            if not is_valid_move(x, y):
                return False

            if grid[x][y] == 'G':
                return True

        return False

    start_pos = None
    goal_pos = None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'G':
                goal_pos = (i, j)

    changes_needed = len(commands)
    for i in range(len(commands)):
        new_commands = commands[:i] + commands[i+1:]
        if simulate_path(new_commands):
            changes_needed = min(changes_needed, 1)

    for i in range(len(commands) + 1):
        for command in ['L', 'R', 'U', 'D']:
            new_commands = commands[:i] + command + commands[i:]
            if simulate_path(new_commands):
                changes_needed = min(changes_needed, 1)

    return changes_needed

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
commands = input().strip()

# Call the function and output the result
print(min_changes_to_fix_program(grid, commands))
