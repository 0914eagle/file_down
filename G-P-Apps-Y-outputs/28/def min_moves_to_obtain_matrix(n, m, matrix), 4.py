
def min_moves_to_obtain_matrix(n, m, matrix):
    target_matrix = [[(i * m) + j for j in range(1, m + 1)] for i in range(n)]
    moves = 0
    
    for j in range(m):
        col_values = [matrix[i][j] for i in range(n)]
        target_col_values = [target_matrix[i][j] for i in range(n)]
        dist = sum(abs(a - b) for a, b in zip(col_values, target_col_values))
        moves = max(moves, dist)
    
    return moves

# Reading input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculating and printing output
print(min_moves_to_obtain_matrix(n, m, matrix))
```
