
def minPath(grid, k):
    n = len(grid)
    visited = set()
    
    def dfs(x, y, path, visited):
        if len(path) == k:
            return path
        
        visited.add((x, y))
        neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
        for nx, ny in neighbors:
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                new_path = dfs(nx, ny, path + [grid[nx][ny]], visited)
                if new_path:
                    return new_path
                
        visited.remove((x, y))
    
    min_path = []
    for i in range(n):
        for j in range(n):
            path = dfs(i, j, [grid[i][j]], visited)
            if path:
                min_path = path
                break
        if min_path:
            break
    
    return min_path

# Test Cases
print(minPath([[1,2,3], [4,5,6], [7,8,9]], 3))  # Output: [1, 2, 1]
print(minPath([[5,9,3], [4,1,6], [7,8,2]], 1))  # Output: [1]
