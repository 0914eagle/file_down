
def transpose(matrix, x, y, k):
    for i in range(x, x+k):
        for j in range(y, y+k):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


def solve(a, b):
    n, m = len(a), len(a[0])
    for k in range(1, min(n, m)+1):
        for x in range(n-k+1):
            for y in range(m-k+1):
                transpose(a, x, y, k)
                if a == b:
                    return "YES"
                transpose(a, x, y, k)
    return "NO"


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]
print(solve(a, b))

