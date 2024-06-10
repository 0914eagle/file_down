
t = int(input())
a = list(map(int, input().split()))

def find_matrix(a):
    n = len(a)
    for i in range(1, n+1):
        if n % i == 0:
            m = n // i
            for x in range(1, i+1):
                for y in range(1, m+1):
                    if check_matrix(a, i, m, x, y):
                        return i, m, x, y
    return -1

def check_matrix(a, n, m, x, y):
    matrix = [[0] * m for _ in range(n)]
    matrix[x-1][y-1] = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                continue
            dist = abs(i-x+1) + abs(j-y+1)
            if dist >= n or dist >= m or matrix[dist][j] != 0 or matrix[i][dist] != 0:
                return False
            matrix[dist][j] = matrix[i][dist] = matrix[i][j]
    return matrix == a

n, m, x, y = find_matrix(a)
if n == -1:
    print(n)
else:
    print(n, m)
    print(x, y)

