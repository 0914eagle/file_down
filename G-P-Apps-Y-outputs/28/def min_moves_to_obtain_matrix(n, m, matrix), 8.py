
def min_moves_to_obtain_matrix(n, m, matrix):
    target_matrix = [[(i * m) + j + 1 for j in range(m)] for i in range(n)]
    moves = 0
    
    for j in range(m):
        col_values = [matrix[i][j] for i in range(n)]
        target_col_values = [target_matrix[i][j] for i in range(n)]
        
        diff = [abs(col_values[i] - target_col_values[i]) for i in range(n)]
        cyclic_shifts = min(sum(diff), n - sum(diff))
        moves += cyclic_shifts
        
    return moves

# Input processing
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the minimum number of moves
print(min_moves_to_obtain_matrix(n, m, matrix))
```
