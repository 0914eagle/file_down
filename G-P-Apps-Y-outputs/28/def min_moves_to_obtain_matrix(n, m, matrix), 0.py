
def min_moves_to_obtain_matrix(n, m, matrix):
    target_matrix = [[(i-1)*m + j for j in range(1, m+1)] for i in range(1, n+1)]
    moves = 0

    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        sorted_col = sorted(col)
        
        if col != sorted_col:
            moves += 1
            for i in range(n):
                matrix[i][j] = sorted_col[i]

    return moves

# Read input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print output
print(min_moves_to_obtain_matrix(n, m, matrix))
```
