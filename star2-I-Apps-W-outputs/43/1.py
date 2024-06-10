
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]

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

for k in range(1, min(n, m) + 1):
    for x in range(n - k + 1):
        for y in range(m - k + 1):
            transpose(a, x, y, k)
            if check(a, b):
                print("YES")
                exit()
            transpose(a, x, y, k)

print("NO")

