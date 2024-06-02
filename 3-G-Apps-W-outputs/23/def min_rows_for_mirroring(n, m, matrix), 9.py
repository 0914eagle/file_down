
def min_rows_for_mirroring(n, m, matrix):
    def is_symmetric(matrix):
        for i in range(len(matrix) // 2):
            if matrix[i] != matrix[len(matrix) - 1 - i]:
                return False
        return True

    for rows in range(1, n + 1):
        if n % rows != 0:
            continue
        valid = True
        for i in range(n // rows):
            submatrix = matrix[i * rows:(i + 1) * rows]
            if not is_symmetric(submatrix):
                valid = False
                break
        if valid:
            return rows

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(min_rows_for_mirroring(n, m, matrix))
