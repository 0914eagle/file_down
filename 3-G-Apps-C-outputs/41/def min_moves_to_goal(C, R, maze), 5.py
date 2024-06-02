
def min_moves_to_goal(C, R, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def valid_move(x, y):
        return 0 <= x < R and 0 <= y < C
    
    def dfs(x, y, moves):
        if maze[x][y] == 'M':
            return 0
        
        min_moves = float('inf')
        
        for dx, dy in directions:
            new_x, new_y = x + dx, y + dy
            
            while valid_move(new_x, new_y) and maze[new_x][new_y] != '#':
                if maze[new_x][new_y] == 'M':
                    min_moves = min(min_moves, moves + 1)
                    break
                new_x += dx
                new_y += dy
            
            if valid_move(new_x, new_y) and maze[new_x][new_y] != '#' and moves + 1 < min_moves:
                min_moves = min(min_moves, dfs(new_x, new_y, moves + 1))
        
        return min_moves if min_moves != float('inf') else -1
    
    result = []
    for i in range(R):
        row = []
        for j in range(C):
            if maze[i][j] == '#':
                row.append(-1)
            else:
                row.append(dfs(i, j, 0))
        result.append(row)
    
    return result

# Input parsing
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

# Compute and output the minimum number of moves needed to reach the goal from each square
result = min_moves_to_goal(C, R, maze)
for row in result:
    print(' '.join(map(str, row)))
