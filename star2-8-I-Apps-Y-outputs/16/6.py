
import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

B = [0] * N
C = [0] * N

B[0] = A[0]
C[N-1] = A[N-1]

for i in range(1, N):
    B[i] = B[i-1] + A[i]
    C[N-1-i] = C[N-i] + A[N-1-i]

for i in range(N):
    print(abs(B[i-1] - C[i]) + abs(B[N-1] - B[i] - C[i]))

