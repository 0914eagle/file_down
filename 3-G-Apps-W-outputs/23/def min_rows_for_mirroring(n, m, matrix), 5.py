
def min_rows_for_mirroring(n, m, matrix):
    def is_symmetric(matrix):
        for i in range(len(matrix) // 2):
            if matrix[i] != matrix[-(i+1)]:
                return False
        return True
    
    for rows in range(1, n+1):
        if n % rows == 0:
            row_groups = [matrix[i:i+rows] for i in range(0, n, rows)]
            if all(is_symmetric(group) for group in row_groups):
                return rows
    
    return n

# Input
n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

# Output
print(min_rows_for_mirroring(n, m, matrix))
