
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

def transpose(matrix, i, j, k):
    for x in range(k):
        for y in range(x+1, k):
            matrix[i+x][j+y], matrix[i+y][j+x] = matrix[i+y][j+x], matrix[i+x][j+y]

for k in range(1, min(n, m)+1):
    for i in range(n-k+1):
        for j in range(m-k+1):
            if a[i][j] != b[i][j]:
                transpose(a, i, j, k)
                if a[i][j] != b[i][j]:
                    print("NO")
                    exit()

print("YES")

