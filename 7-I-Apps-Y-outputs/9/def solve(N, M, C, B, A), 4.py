
import sys

def solve(N, M, C, B, A):
    count = 0
    for i in range(N):
        sum = 0
        for j in range(M):
            sum += A[i][j] * B[j]
        if sum + C > 0:
            count += 1
    return count

if __name__ == '__main__':
    N, M, C = map(int, sys.stdin.readline().split())
    B = list(map(int, sys.stdin.readline().split()))
    A = []
    for i in range(N):
        A.append(list(map(int, sys.stdin.readline().split())))
    print(solve(N, M, C, B, A))

