
def shortest_ladder_length(M, N, vault):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    def bfs(height):
        visited = set()
        queue = [(0, 0)]
        
        while queue:
            x, y = queue.pop(0)
            visited.add((x, y))
            
            if x == M-1 and y == N-1:
                return True
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < M and 0 <= ny < N and (nx, ny) not in visited and abs(vault[nx][ny] - vault[x][y]) <= height:
                    queue.append((nx, ny))
        
        return False
    
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        if bfs(mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Input parsing
M, N = map(int, input().split())
vault = [list(map(int, input().split())) for _ in range(M)]

result = shortest_ladder_length(M, N, vault)
print(result)
```
