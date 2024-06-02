
def min_moves_to_goal(C, R, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves_needed = [[-1 for _ in range(C)] for _ in range(R)]
    
    def is_valid_move(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def dfs(x, y, moves):
        if not is_valid_move(x, y) or maze[x][y] == '#':
            return
        if moves_needed[x][y] != -1 and moves >= moves_needed[x][y]:
            return
        moves_needed[x][y] = moves
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            while is_valid_move(new_x, new_y) and maze[new_x][new_y] != '#':
                if moves_needed[new_x][new_y] == -1 or moves < moves_needed[new_x][new_y]:
                    dfs(new_x, new_y, moves)
                new_x, new_y = new_x + dx, new_y + dy
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'M':
                dfs(i, j, 0)
    
    for row in moves_needed:
        print(' '.join(map(str, row)))

# Input parsing
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

min_moves_to_goal(C, R, maze)
