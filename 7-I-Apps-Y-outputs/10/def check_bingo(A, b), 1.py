
def check_bingo(A, b):
    # Write your code here
    for i in range(len(b)):
        if b[i] in A:
            A.remove(b[i])
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] in b:
                b.remove(A[i][j])
    for i in range(len(A)):
        if A[i][0] in b and A[i][1] in b and A[i][2] in b:
            return True
        if A[0][i] in b and A[1][i] in b and A[2][i] in b:
            return True
    if A[0][0] in b and A[1][1] in b and A[2][2] in b:
        return True
    if A[0][2] in b and A[1][1] in b and A[2][0] in b:
        return True
    return False

