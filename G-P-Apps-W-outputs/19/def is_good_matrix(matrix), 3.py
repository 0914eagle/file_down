
def is_good_matrix(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 1:
                for k in range(i, n):
                    for l in range(j, m):
                        if (k - i + 1) % 2 == 0 and (l - j + 1) % 2 == 0:
                            ones_count = 0
                            for x in range(i, k+1):
                                for y in range(j, l+1):
                                    if matrix[x][y] == 1:
                                        ones_count += 1
                            if ones_count % 2 == 0:
                                return False
    return True

def min_cells_to_change(n, m, matrix):
    if is_good_matrix(matrix):
        return 0

    ones_count = sum(row.count(1) for row in matrix)
    if ones_count % 2 == 1:
        return -1
    return min(ones_count, n*m - ones_count)

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
print(min_cells_to_change(n, m, matrix))
```
