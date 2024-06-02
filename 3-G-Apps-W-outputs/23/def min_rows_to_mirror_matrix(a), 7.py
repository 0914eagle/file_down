
def min_rows_to_mirror_matrix(a):
    n = len(a)
    m = len(a[0])
    
    for rows in range(1, n+1):
        if n % rows == 0:
            valid = True
            for i in range(rows // 2):
                if a[i] != a[rows - 1 - i]:
                    valid = False
                    break
            if valid:
                return rows
    
    return n

# Read input
n, m = map(int, input().split())
matrix_a = [list(map(int, input().split())) for _ in range(n)]

# Find minimum number of rows for mirroring matrix
result = min_rows_to_mirror_matrix(matrix_a)
print(result)
