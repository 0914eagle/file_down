
def is_good(matrix):
    rows, cols = len(matrix), len(matrix[0])
    
    for r1 in range(rows):
        for r2 in range(r1, rows):
            for c1 in range(cols):
                for c2 in range(c1, cols):
                    if (r2 - r1 + 1) % 2 == 0 and (c2 - c1 + 1) % 2 == 0:
                        count_ones = sum(matrix[i][j] for i in range(r1, r2 + 1) for j in range(c1, c2 + 1))
                        if count_ones % 2 == 0:
                            return False
    return True

def min_cells_to_change(n, m, matrix):
    if is_good(matrix):
        return 0
    
    count_ones = sum(row.count('1') for row in matrix)
    count_zeros = n * m - count_ones
    
    if count_ones % 2 == 1 and count_zeros % 2 == 1:
        return -1
    
    return min(count_ones, count_zeros)

# Input parsing
n, m = map(int, input().split())
matrix = [input().strip() for _ in range(n)]

# Output
print(min_cells_to_change(n, m, matrix))
