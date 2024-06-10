
def fishing(r, c, k, l, x0, y0, t):
    grid = [[0 for i in range(c)] for j in range(r)]
    for i in range(r):
        for j in range(c):
            if t[i][j] + k > l:
                continue
            grid[i][j] = 1
            
    visited = [[False for i in range(c)] for j in range(r)]
    
    queue = [(x0, y0)]
    visited[x0][y0] = True
    
    max_count = 0
    
    while len(queue) > 0:
        curr_x, curr_y = queue.pop(0)
        
        max_count += 1
        
        for x, y in [(curr_x+1, curr_y), (curr_x-1, curr_y), (curr_x, curr_y+1), (curr_x, curr_y-1)]:
            if 0 <= x < r and 0 <= y < c and not visited[x][y] and grid[x][y] == 1:
                queue.append((x, y))
                visited[x][y] = True
    
    return max_count

