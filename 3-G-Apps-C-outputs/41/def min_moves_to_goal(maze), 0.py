
def min_moves_to_goal(maze):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def valid_move(row, col):
        return 0 <= row < rows and 0 <= col < cols
    
    def bfs(start_row, start_col):
        queue = [(start_row, start_col, 0)]
        visited = set()
        
        while queue:
            row, col, moves = queue.pop(0)
            
            if maze[row][col] == 'M':
                return moves
            
            visited.add((row, col))
            
            for dr, dc in directions:
                new_row, new_col = row + dr, col + dc
                
                while valid_move(new_row, new_col) and maze[new_row][new_col] != '#':
                    if (new_row, new_col) not in visited:
                        queue.append((new_row, new_col, moves + 1))
                        visited.add((new_row, new_col))
                    
                    if maze[new_row][new_col] == '_':
                        new_row += dr
                        new_col += dc
                    else:
                        break
        
        return -1
    
    result = [[-1 for _ in range(cols)] for _ in range(rows)]
    
    for i in range(rows):
        for j in range(cols):
            if maze[i][j] != '#':
                result[i][j] = bfs(i, j)
    
    return result

# Input parsing
C, R = map(int, input().split())
maze = [list(input().strip()) for _ in range(R)]

# Compute minimum moves to goal for each square in the maze
result = min_moves_to_goal(maze)

# Output the result
for row in result:
    print(' '.join(map(str, row)))
