
from collections import deque

def minimum_moves_to_goal(C, R, maze):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    moves_needed = [[-1 for _ in range(C)] for _ in range(R)]
    
    def is_valid_move(x, y):
        return 0 <= x < R and 0 <= y < C and maze[x][y] != '#'
    
    def bfs(start_x, start_y):
        queue = deque([(start_x, start_y, 0)])
        visited = set()
        
        while queue:
            x, y, moves = queue.popleft()
            if moves_needed[x][y] == -1 or moves < moves_needed[x][y]:
                moves_needed[x][y] = moves
            visited.add((x, y))
            
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                new_moves = moves + 1
                
                while is_valid_move(new_x, new_y):
                    if moves_needed[new_x][new_y] == -1 or new_moves < moves_needed[new_x][new_y]:
                        moves_needed[new_x][new_y] = new_moves
                    if maze[new_x][new_y] == 'M':
                        break
                    new_x, new_y = new_x + dx, new_y + dy
                    new_moves += 1
                
                if (new_x, new_y) not in visited:
                    queue.append((new_x, new_y, new_moves))
    
    for i in range(R):
        for j in range(C):
            if maze[i][j] == 'M':
                bfs(i, j)
    
    return moves_needed

# Input parsing
C, R = map(int, input().split())
maze = [input() for _ in range(R)]

# Compute minimum moves to goal
result = minimum_moves_to_goal(C, R, maze)

# Output
for row in result:
    print(' '.join(map(str, row)))

