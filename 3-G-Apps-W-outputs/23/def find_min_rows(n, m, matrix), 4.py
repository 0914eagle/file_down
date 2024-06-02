
def find_min_rows(n, m, matrix):
    def is_mirrorable(matrix):
        for i in range(len(matrix)):
            if matrix[i] != matrix[-i-1]:
                return False
        return True

    for rows in range(1, n+1):
        if n % rows == 0:
            block_size = n // rows
            blocks = [matrix[i:i+block_size] for i in range(0, n, block_size)]
            if all(is_mirrorable(block) for block in blocks):
                return rows

n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

result = find_min_rows(n, m, matrix)
print(result)
