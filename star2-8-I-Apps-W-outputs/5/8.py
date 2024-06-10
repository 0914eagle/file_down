

def find_path(n, m, k, maze):
    
    def valid_pos(pos):
        return pos[0] >= 0 and pos[0] < n and pos[1] >= 0 and pos[1] < m
    
    start = (-1, -1)
    
    for i in range(n):
        for j in range(m):
            if maze[i][j] == 'X':
                start = (i, j)
    
    stack = [(start, '')]
    
    while stack:
        pos, path = stack.pop()
        
        if len(path) == k:
            if pos == start:
                return path
        
        for i in range(4):
            new_pos = (pos[0] + dx[i], pos[1] + dy[i])
            
            if valid_pos(new_pos) and maze[new_pos[0]][new_pos[1]] == '.' and new_pos not in path:
                stack.append((new_pos, path + directions[i]))
    
    return 'IMPOSSIBLE'


n, m, k = map(int, input().split())
maze = [input() for _ in range(n)]

directions = 'DLRU'
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

print(find_path(n, m, k, maze))


