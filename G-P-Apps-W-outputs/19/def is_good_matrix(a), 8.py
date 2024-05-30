
def is_good_matrix(a):
    n, m = len(a), len(a[0])
    for i in range(n-1):
        for j in range(m-1):
            if (i+2 <= n and j+2 <= m) and ((i+j) % 2 == 0):
                sub_matrix_ones = a[i][j] + a[i+1][j] + a[i][j+1] + a[i+1][j+1]
                if sub_matrix_ones % 2 == 0:
                    return False
    return True

def min_cells_to_change(n, m, matrix):
    a = [[int(matrix[i][j]) for j in range(m)] for i in range(n)]
    
    if is_good_matrix(a):
        return 0
    
    if n < 2 or m < 2:
        return -1
    
    count = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 0:
                a[i][j] = 1
                if is_good_matrix(a):
                    return 1
                a[i][j] = 0
                
            else:
                a[i][j] = 0
                if is_good_matrix(a):
                    return 1
                a[i][j] = 1
    
    return -1

# Input
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Output
print(min_cells_to_change(n, m, matrix))

```
