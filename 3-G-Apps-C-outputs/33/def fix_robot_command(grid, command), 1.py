
def fix_robot_command(grid, command):
    def is_valid_move(x, y):
        return 0 <= x < len(grid) and 0 <= y < len(grid[0]) and grid[x][y] != '#'
    
    def dfs(x, y, idx):
        if idx == len(command):
            return 0
        
        changes = float('inf')
        dx, dy = {'L': 0, 'R': 0, 'U': -1, 'D': 1}[command[idx]]
        if is_valid_move(x + dx, y + dy):
            changes = min(changes, dfs(x + dx, y + dy, idx + 1))
        
        for new_command in ['L', 'R', 'U', 'D']:
            if new_command != command[idx]:
                dx, dy = {'L': 0, 'R': 0, 'U': -1, 'D': 1}[new_command]
                if is_valid_move(x + dx, y + dy):
                    changes = min(changes, 1 + dfs(x + dx, y + dy, idx))
        
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

# Read input
H, W = map(int, input().split())
grid = [input() for _ in range(H)]
command = input()

# Call the function and output the result
print(fix_robot_command(grid, command))
