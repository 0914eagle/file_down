
def transpose(matrix, n, m, x, y, k):
    for i in range(k):
        for j in range(k):
            matrix[x + i][y + j], matrix[x + j][y + i] = matrix[x + j][y + i], matrix[x + i][y + j]


def solve(a, b, n, m):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                for k in range(1, min(n - i, m - j) + 1):
                    for x in range(n - k + 1):
                        for y in range(m - k + 1):
                            transpose(a, n, m, x, y, k)
                            if a[i][j] == b[i][j]:
                                return True
                            transpose(a, n, m, x, y, k)
    return False


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
if solve(a, b, n, m):
    print("YES")
else:
    print("NO")

