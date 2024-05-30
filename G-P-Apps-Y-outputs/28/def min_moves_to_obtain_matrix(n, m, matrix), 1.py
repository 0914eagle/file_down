
def min_moves_to_obtain_matrix(n, m, matrix):
    target_matrix = [[(i - 1) * m + j for j in range(1, m + 1)] for i in range(1, n + 1)]

    moves = 0
    for j in range(m):
        col = [matrix[i][j] for i in range(n)]
        target_col = [target_matrix[i][j] for i in range(n)]
        
        cyclic_shifts = []
        for k in range(n):
            shifts = []
            for l in range(n):
                shifted_col = col[-l:] + col[:-l]
                if shifted_col == target_col:
                    shifts.append(l)
            cyclic_shifts.append(min(shifts))
            col = col[-1:] + col[:-1]

        moves += min(cyclic_shifts)

    return moves

# Input parsing
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_moves_to_obtain_matrix(n, m, matrix))
