
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'
    
    def execute_command(x, y, cmd):
        if cmd == 'L':
            return x, y - 1
        elif cmd == 'R':
            return x, y + 1
        elif cmd == 'U':
            return x - 1, y
        elif cmd == 'D':
            return x + 1, y
        return x, y
    
    def simulate_command_changes(changes):
        x, y = start_pos
        for cmd in command:
            dx, dy = execute_command(x, y, cmd)
            if is_valid_move(dx, dy):
                x, y = dx, dy
            else:
                changes -= 1
                if changes < 0:
                    return False
        return True
    
    H, W = len(grid), len(grid[0])
    start_pos, goal_pos = None, None
    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start_pos = (i, j)
            elif grid[i][j] == 'G':
                goal_pos = (i, j)
    
    changes = 0
    while not simulate_command_changes(changes):
        changes += 1
    
    return changes

# Input parsing
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
command = input().strip()

result = fix_robot_command(grid, command)
print(result)
