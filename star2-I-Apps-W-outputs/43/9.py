
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

def transpose(matrix, x, y, k):
    for i in range(x, x + k):
        for j in range(y, y + k):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def check(a, b):
    for i in range(n):
        for j in range(m):
            if a[i][j] != b[i][j]:
                return False
    return True

for k in range(min(n, m), 0, -1):
    for i in range(n - k + 1):
        for j in range(m - k + 1):
            transpose(a, i, j, k)
            if check(a, b):
                print("YES")
                exit()
            transpose(a, i, j, k)

print("NO")

