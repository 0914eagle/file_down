
def solution(N, M, C, B, A):
    # write your code in Python 3.6
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    return count

