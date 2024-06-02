
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'
    
    def execute_command(cmd):
        nonlocal x, y
        if cmd == 'L':
            if is_valid_move(x, y - 1):
                y -= 1
        elif cmd == 'R':
            if is_valid_move(x, y + 1):
                y += 1
        elif cmd == 'U':
            if is_valid_move(x - 1, y):
                x -= 1
        elif cmd == 'D':
            if is_valid_move(x + 1, y):
                x += 1
    
    def simulate_command_sequence(cmd_sequence):
        nonlocal x, y
        for cmd in cmd_sequence:
            execute_command(cmd)
            if grid[x][y] == 'G':
                return True
        return False
    
    h, w = len(grid), len(grid[0])
    x, y = 0, 0
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 'S':
                x, y = i, j
                break
    
    changes_needed = float('inf')
    for i in range(len(command) + 1):
        for new_cmd in 'LRUD':
            new_command = command[:i] + new_cmd + command[i:]
            if simulate_command_sequence(new_command):
                changes_needed = min(changes_needed, abs(len(command) - len(new_command)))
    
    return changes_needed

# Read input
h, w = map(int, input().split())
grid = [input() for _ in range(h)]
command = input()

# Call the function and output the result
print(fix_robot_command(grid, command))
