
import sys

N = int(input())

C = []
S = []
F = []

for i in range(N):
    C.append(list(map(int, sys.stdin.readline().split())))
    S.append(C[i][0])
    F.append(C[i][1])

for i in range(1, N):
    S[i] += S[i - 1] + C[i - 1][0]

for i in range(N - 1):
    F[i] = S[i] % F[i]

for i in range(N - 1, 0, -1):
    print(S[i] - F[i - 1])

