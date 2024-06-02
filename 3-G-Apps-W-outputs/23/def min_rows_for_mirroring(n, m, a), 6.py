
def min_rows_for_mirroring(n, m, a):
    def is_symmetric(matrix):
        for i in range(len(matrix) // 2):
            if matrix[i] != matrix[-i-1]:
                return False
        return True

    for rows in range(1, n+1):
        if n % rows != 0:
            continue
        b = [a[i:i+rows] for i in range(0, n, rows)]
        if all(is_symmetric(row) for row in b):
            return rows

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

print(min_rows_for_mirroring(n, m, a))
