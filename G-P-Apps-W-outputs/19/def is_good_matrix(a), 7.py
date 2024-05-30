
def is_good_matrix(a):
    n = len(a)
    m = len(a[0])
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == '1':
                a[i][j] = 1
            else:
                a[i][j] = 0
    
    prefix_sum = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] - prefix_sum[i-1][j-1] + a[i-1][j-1]
    
    def get_sum(r1, c1, r2, c2):
        return prefix_sum[r2][c2] - prefix_sum[r1-1][c2] - prefix_sum[r2][c1-1] + prefix_sum[r1-1][c1-1]
    
    for size in range(2, min(n, m) + 1, 2):
        for i in range(n - size + 1):
            for j in range(m - size + 1):
                sub_sum = get_sum(i+1, j+1, i+size, j+size)
                if sub_sum % 2 == 0:
                    return False
    
    return True

def min_cells_to_change(n, m, matrix):
    a = [list(row) for row in matrix]
    if is_good_matrix(a):
        return 0
    
    for i in range(n):
        for j in range(m):
            original = a[i][j]
            a[i][j] = 1 if a[i][j] == 0 else 0
            if is_good_matrix(a):
                return 1
            a[i][j] = original
    
    return -1

# Input processing
n, m = map(int, input().split())
matrix = [input() for _ in range(n)]

# Output the result
print(min_cells_to_change(n, m, matrix))
```
