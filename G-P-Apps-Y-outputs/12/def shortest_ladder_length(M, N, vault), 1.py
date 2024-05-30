
def shortest_ladder_length(M, N, vault):
    def can_reach(vault, ladder_length):
        visited = set()
        stack = [(0, 0)]
        
        while stack:
            i, j = stack.pop()
            if i == M-1 and j == N-1:
                return True
            
            visited.add((i, j))
            for x, y in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= x < M and 0 <= y < N and (x, y) not in visited and abs(vault[i][j] - vault[x][y]) <= ladder_length:
                    stack.append((x, y))
        
        return False
    
    left, right = 0, 10**9
    while left < right:
        mid = (left + right) // 2
        if can_reach(vault, mid):
            right = mid
        else:
            left = mid + 1
    
    return left

# Read input
M, N = map(int, input().split())
vault = [list(map(int, input().split())) for _ in range(M)]

# Output result
print(shortest_ladder_length(M, N, vault))
```
