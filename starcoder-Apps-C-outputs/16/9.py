
n, m = map(int, input().split())
matrix = [[0 for i in range(n)] for i in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    matrix[a][b] += c
    matrix[b][a] += c

for i in range(n):
    for j in range(i + 1, n):
        if matrix[i][j] != 0:
            break
    if j == n - 1:
        break

if i != j:
    print(n * (n - 1) // 2)
    for i in range(n):
        for j in range(i + 1, n):
            if matrix[i][j] != 0:
                print(i, j, matrix[i][j] // 2)
else:
    print(0)
