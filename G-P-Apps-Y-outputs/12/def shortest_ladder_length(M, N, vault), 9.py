
def shortest_ladder_length(M, N, vault):
    def can_reach(vault, ladder_length):
        stack = [(0, 0, ladder_length)]
        visited = set()
        
        while stack:
            row, col, length = stack.pop()
            if (row, col) in visited:
                continue
            visited.add((row, col))
            
            if row == M - 1 and col == N - 1:
                return True
            
            height = vault[row][col]
            
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_row, new_col = row + dr, col + dc
                
                if 0 <= new_row < M and 0 <= new_col < N:
                    new_height = vault[new_row][new_col]
                    if abs(new_height - height) <= length:
                        stack.append((new_row, new_col, max(length, abs(new_height - height))))
        
        return False
    
    low, high = 0, max(M, N, max(max(row) for row in vault))
    
    while low < high:
        mid = (low + high) // 2
        if can_reach(vault, mid):
            high = mid
        else:
            low = mid + 1
    
    return low

# Input parsing
input_line = input().strip().split()
M, N = int(input_line[0]), int(input_line[1])
vault = [list(map(int, input().strip().split())) for _ in range(M)]

print(shortest_ladder_length(M, N, vault))
```
