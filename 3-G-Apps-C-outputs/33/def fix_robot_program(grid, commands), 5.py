
def fix_robot_program(grid, commands):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def execute_command(x, y, command):
        if command == 'L':
            return x, y - 1 if is_valid_move(x, y - 1) else y
        elif command == 'R':
            return x, y + 1 if is_valid_move(x, y + 1) else y
        elif command == 'U':
            return x - 1, y if is_valid_move(x - 1, y) else y
        elif command == 'D':
            return x + 1, y if is_valid_move(x + 1, y) else y

    def simulate(commands):
        x, y = start
        for command in commands:
            x, y = execute_command(x, y, command)
            if grid[x][y] == 'G':
                return True
        return False

    def min_changes(commands):
        changes = 0
        while not simulate(commands):
            changes += 1
            for i in range(len(commands)):
                new_commands = commands[:i] + commands[i+1:]
                if simulate(new_commands):
                    return changes
            for i in range(len(commands) + 1):
                for c in 'LRUD':
                    new_commands = commands[:i] + c + commands[i:]
                    if simulate(new_commands):
                        return changes
        return changes

    start = None
    goal = None

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    return min_changes(commands)

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
commands = input()

# Call the function and output the result
print(fix_robot_program(grid, commands))
