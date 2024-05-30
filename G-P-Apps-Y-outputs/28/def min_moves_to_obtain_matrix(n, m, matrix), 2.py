
def min_moves_to_obtain_matrix(n, m, matrix):
    target = [[(i * m) + j for j in range(1, m + 1)] for i in range(n)]
    moves = 0
    
    for j in range(m):
        column = [matrix[i][j] for i in range(n)]
        diff = [abs(column[i] - target[i][j]) for i in range(n)]
        max_diff = max(diff)
        moves += min(max_diff, n * m - max_diff)
    
    return moves

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_moves_to_obtain_matrix(n, m, matrix))
```
