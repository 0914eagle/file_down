
def transpose(matrix, x, y, k):
    for i in range(k):
        for j in range(i + 1, k):
            matrix[x + i][y + j], matrix[x + j][y + i] = matrix[x + j][y + i], matrix[x + i][y + j]


def solve(a, b):
    n, m = len(a), len(a[0])
    for k in range(1, min(n, m) + 1):
        for i in range(n - k + 1):
            for j in range(m - k + 1):
                transpose(a, i, j, k)
                if a == b:
                    return "YES"
                transpose(a, i, j, k)
    return "NO"


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
print(solve(a, b))

