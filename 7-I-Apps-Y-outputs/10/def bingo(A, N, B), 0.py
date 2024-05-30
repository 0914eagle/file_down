
def bingo(A, N, B):
    # Write your code here
    for i in range(3):
        for j in range(3):
            if A[i][j] in B:
                B.remove(A[i][j])
    if len(B) == 0:
        return "Yes"
    else:
        return "No"

