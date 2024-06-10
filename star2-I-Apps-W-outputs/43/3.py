
n, m = map(int, input().split())
A = [list(map(int, input().split())) for i in range(n)]
B = [list(map(int, input().split())) for i in range(n)]

def transpose(matrix, x, y, k):
    for i in range(k):
        for j in range(i+1, k):
            matrix[x+i][y+j], matrix[x+j][y+i] = matrix[x+j][y+i], matrix[x+i][y+j]

def check(A, B):
    if A == B:
        return True
    n, m = len(A), len(A[0])
    for k in range(min(n, m), 0, -1):
        for i in range(n-k+1):
            for j in range(m-k+1):
                transpose(A, i, j, k)
                if A == B:
                    return True
                transpose(A, i, j, k)
    return False

if check(A, B):
    print("YES")
else:
    print("NO")

