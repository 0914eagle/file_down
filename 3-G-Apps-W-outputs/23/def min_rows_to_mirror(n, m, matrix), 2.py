
def min_rows_to_mirror(n, m, matrix):
    def is_mirrorable(matrix):
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != matrix[n*2-1-i][j]:
                    return False
        return True

    for i in range(1, n+1):
        if n % i == 0:
            sub_matrix = [matrix[j:j+i] for j in range(0, n, i)]
            if is_mirrorable(sub_matrix):
                return i

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
print(min_rows_to_mirror(n, m, matrix))
