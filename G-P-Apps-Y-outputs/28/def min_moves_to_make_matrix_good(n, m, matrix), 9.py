
def min_moves_to_make_matrix_good(n, m, matrix):
    moves = 0
    
    for j in range(m):
        col_values = [matrix[i][j] for i in range(n)]
        target_col_values = [(i * m) + j + 1 for i in range(n)]
        
        diff = sum(abs(col_values[k] - target_col_values[k]) for k in range(n))
        cyclic_shifts = 0
        
        for k in range(1, n):
            cyclic_shifts = max(cyclic_shifts, col_values[k] - target_col_values[k])
        
        moves += min(diff, cyclic_shifts, n - cyclic_shifts)
    
    return moves

# Input parsing
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output the result
print(min_moves_to_make_matrix_good(n, m, matrix))
