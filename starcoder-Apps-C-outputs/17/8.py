
import numpy as np

N, M = map(int, input().split())

A = np.zeros((M, M), dtype = int)
B = np.zeros(M, dtype = int)

for i in range(N):
  D1, M1, D2, M2, F = map(int, input().split())
  F = np.array(F, dtype = int)
  A[0] += F
  B += F
  A[i + 1] = F
  B -= F

#print(A)
#print(B)

if np.linalg.matrix_rank(A) != M:
  print(-1)
  exit()

#print(np.linalg.solve(A, B))
ans = np.linalg.solve(A, B)

if np.any(ans < 0):
  print(-1)
else:
  print(*ans, sep = " ")
