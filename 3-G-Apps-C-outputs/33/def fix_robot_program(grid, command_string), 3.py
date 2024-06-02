
def fix_robot_program(grid, command_string):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'

    def execute_command(x, y, command):
        if command == 'L':
            return x, y - 1
        elif command == 'R':
            return x, y + 1
        elif command == 'U':
            return x - 1, y
        elif command == 'D':
            return x + 1, y
        return x, y

    def simulate_path(command_string):
        x, y = start
        for command in command_string:
            new_x, new_y = execute_command(x, y, command)
            if is_valid_move(new_x, new_y):
                x, y = new_x, new_y
            if grid[x][y] == 'G':
                return True
        return False

    h, w = len(grid), len(grid[0])
    start, goal = None, None

    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)

    changes_needed = 0
    if not simulate_path(command_string):
        changes_needed = 1

        for i in range(len(command_string) + 1):
            for command in ['L', 'R', 'U', 'D']:
                new_command_string = command_string[:i] + command + command_string[i:]
                if simulate_path(new_command_string):
                    return changes_needed

        changes_needed = 2

    return changes_needed

# Read input
h, w = map(int, input().split())
grid = [input() for _ in range(h)]
command_string = input()

# Output the result
print(fix_robot_program(grid, command_string))
