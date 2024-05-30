
def is_good(matrix):
    n = len(matrix)
    m = len(matrix[0])
    
    def count_ones(r1, r2, c1, c2):
        return sum(matrix[i][j] for i in range(r1, r2+1) for j in range(c1, c2+1))
    
    for r1 in range(n):
        for r2 in range(r1+1, n+1):
            for c1 in range(m):
                for c2 in range(c1+1, m+1):
                    if (r2 - r1) % 2 == 0 and (c2 - c1) % 2 == 0:
                        ones_count = count_ones(r1, r2, c1, c2)
                        if ones_count % 2 == 0:
                            return False
    return True

def min_cells_to_change(n, m, matrix):
    if is_good(matrix):
        return 0

    for i in range(n):
        for j in range(m):
            matrix[i][j] = 1 - matrix[i][j]
            if is_good(matrix):
                return 1
            matrix[i][j] = 1 - matrix[i][j]

    return -1

n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]
print(min_cells_to_change(n, m, matrix))
