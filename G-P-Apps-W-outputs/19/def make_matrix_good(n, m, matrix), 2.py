
def make_matrix_good(n, m, matrix):
    def count_ones_in_submatrix(r1, r2, c1, c2):
        return sum(matrix[i][j] for i in range(r1, r2+1) for j in range(c1, c2+1))

    def is_odd(num):
        return num % 2 != 0

    changes_needed = 0

    for i in range(n):
        for j in range(m):
            if is_odd(n - i) and is_odd(m - j) and is_odd(i + j + 2):
                ones_count = count_ones_in_submatrix(max(1, i-1), min(n, i+1), max(1, j-1), min(m, j+1))
                if not is_odd(ones_count):
                    changes_needed += 1

    if (n * m) % 2 != changes_needed % 2:
        return -1

    return changes_needed

# Reading input
n, m = map(int, input().split())
matrix = [list(map(int, input().strip())) for _ in range(n)]

# Output result
result = make_matrix_good(n, m, matrix)
print(result)
