
def min_cells_to_change(n, m, matrix):
    def is_good(matrix):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 1 and (i+j) % 2 == 0:
                    return False
        return True

    def count_ones_in_submatrix(r1, r2, c1, c2):
        return sum(matrix[i][j] for i in range(r1, r2+1) for j in range(c1, c2+1))

    count = 0
    for r1 in range(1, n+1):
        for r2 in range(r1, n+1):
            for c1 in range(1, m+1):
                for c2 in range(c1, m+1):
                    if (r2-r1+1) % 2 == 0 and (c2-c1+1) % 2 == 0:
                        ones_count = count_ones_in_submatrix(r1, r2, c1, c2)
                        if ones_count % 2 == 0:
                            count += 1
    return count if is_good(matrix) else -1

# Input processing
n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

# Output
print(min_cells_to_change(n, m, matrix))
