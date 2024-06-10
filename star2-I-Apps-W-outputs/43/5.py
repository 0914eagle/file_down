
n, m = map(int, input().split())
a = [list(map(int, input().split())) for i in range(n)]
b = [list(map(int, input().split())) for i in range(n)]

def transpose(a, x, y, k):
    for i in range(k):
        for j in range(i + 1, k):
            a[x + i][y + j], a[x + j][y + i] = a[x + j][y + i], a[x + i][y + j]

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
                exit(0)
            transpose(a, i, j, k)

print("NO")

