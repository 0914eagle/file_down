
def min_moves_to_goal(maze):
    rows = len(maze)
    cols = len(maze[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def is_valid_move(row, col):
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
                
                if is_valid_move(new_row, new_col) and (new_row, new_col) not in visited:
                    if maze[new_row][new_col] == '.' or maze[new_row][new_col] == 'M':
                        queue.append((new_row, new_col, moves + 1))
                    elif maze[new_row][new_col] == '_':
                        queue.append((new_row, new_col, moves + 1))
                        while is_valid_move(new_row + dr, new_col + dc) and maze[new_row + dr][new_col + dc] == '_':
                            new_row += dr
                            new_col += dc
                            queue.append((new_row, new_col, moves + 1))
        
        return -1
    
    result = []
    for i in range(rows):
        row_result = []
        for j in range(cols):
            if maze[i][j] == '#':
                row_result.append(-1)
            else:
                row_result.append(bfs(i, j))
        result.append(row_result)
    
    return result

# Read input
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

# Compute and print output
result = min_moves_to_goal(maze)
for row in result:
    print(' '.join(map(str, row)))
