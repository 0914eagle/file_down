
def shortest_ladder_length(M, N, vault):
    def can_reach_target(ladder_length):
        stack = [(0, 0, ladder_length)]
        visited = set()
        
        while stack:
            i, j, ladder = stack.pop()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if i == M - 1 and j == N - 1:
                return True
            
            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                ni, nj = i + dx, j + dy
                if 0 <= ni < M and 0 <= nj < N:
                    next_ladder = max(ladder, abs(vault[ni][nj] - vault[i][j]))
                    if next_ladder < vault[ni][nj]:
                        stack.append((ni, nj, next_ladder))
        
        return False
    
    low, high = 0, 10**9
    while low < high:
        mid = (low + high) // 2
        if can_reach_target(mid):
            high = mid
        else:
            low = mid + 1
    
    return low

# Input parsing
input_data = input().split()
M, N = int(input_data[0]), int(input_data[1])
vault = []
for _ in range(M):
    row = list(map(int, input().split()))
    vault.append(row)

# Calculate and output the result
print(shortest_ladder_length(M, N, vault))
```
