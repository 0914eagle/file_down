
def fix_robot_command(H, W, grid, commands):
    start = None
    goal = None
    obstacles = set()

    for i in range(H):
        for j in range(W):
            if grid[i][j] == 'S':
                start = (i, j)
            elif grid[i][j] == 'G':
                goal = (i, j)
            elif grid[i][j] == '#':
                obstacles.add((i, j))

    def is_valid_move(pos):
        return 0 <= pos[0] < H and 0 <= pos[1] < W and pos not in obstacles

    def simulate(commands):
        pos = start
        for cmd in commands:
            if cmd == 'L':
                new_pos = (pos[0], pos[1] - 1)
            elif cmd == 'R':
                new_pos = (pos[0], pos[1] + 1)
            elif cmd == 'U':
                new_pos = (pos[0] - 1, pos[1])
            elif cmd == 'D':
                new_pos = (pos[0] + 1, pos[1])

            if is_valid_move(new_pos):
                pos = new_pos
                if pos == goal:
                    return True
        return False

    changes_needed = float('inf')
    for i in range(len(commands) + 1):
        for cmd in ['L', 'R', 'U', 'D']:
            new_commands = commands[:i] + cmd + commands[i:]
            if simulate(new_commands):
                changes_needed = min(changes_needed, abs(len(commands) - len(new_commands)))

    return changes_needed

# Input parsing
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
commands = input().strip()

# Call the function and print the output
print(fix_robot_command(H, W, grid, commands))
