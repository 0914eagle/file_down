
def min_moves_to_obtain_matrix(n, m, matrix):
    moves = 0

    for j in range(m):
        curr_col = [matrix[i][j] for i in range(n)]
        target_col = [(i - 1) * m + j + 1 for i in range(1, n + 1)]
        
        diff = [abs(curr_col[i] - target_col[i]) for i in range(n)]
        max_diff = max(diff)
        
        moves += min(max_diff, m - max_diff)
    
    return moves

# Reading input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_moves_to_obtain_matrix(n, m, matrix))
