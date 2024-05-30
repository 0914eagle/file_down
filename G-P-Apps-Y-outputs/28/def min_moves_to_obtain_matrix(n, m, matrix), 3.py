
def min_moves_to_obtain_matrix(n, m, matrix):
    expected_value = 1
    moves = 0
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] != expected_value:
                moves += min(abs(matrix[i][j] - expected_value), n * m - abs(matrix[i][j] - expected_value))
        
            expected_value += 1
    
    return moves

# Input parsing
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print the minimum number of moves required
print(min_moves_to_obtain_matrix(n, m, matrix))
