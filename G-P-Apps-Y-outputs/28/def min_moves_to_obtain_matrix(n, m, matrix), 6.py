
def min_moves_to_obtain_matrix(n, m, matrix):
    target_matrix = [[(i-1)*m+j for j in range(1, m+1)] for i in range(1, n+1)]

    moves = 0
    for j in range(m):
        col_values = [matrix[i][j] for i in range(n)]
        target_col_values = target_matrix[0][j]
        shift_distance = (target_col_values - col_values[0]) % (n*m)
        moves += min(shift_distance, n*m - shift_distance)

    return moves

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_moves_to_obtain_matrix(n, m, matrix))
```
