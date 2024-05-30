
def min_moves_to_match_matrix(n, m, matrix):
    moves = 0
    for j in range(m):
        target_column = [(i - 1) * m + j + 1 for i in range(1, n + 1)]
        current_column = [matrix[i][j] for i in range(n)]
        
        diff = [target_column[i] - current_column[i] for i in range(n)]
        for i in range(1, n):
            if diff[i] <= 0:
                diff[i] += n * m
        
        max_diff = max(diff)
        moves += max_diff
        
        for i in range(n):
            matrix[i][j] += max_diff
    
    return moves

# Read input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Call the function and print the output
print(min_moves_to_match_matrix(n, m, matrix))
```
