
import numpy as np
import math
from queue import Queue

def solve(A, t):
	N = A.shape[0]
	C = np.zeros((N, N))
	for i in range(N):
		for j in range(N):
			if i > 0 and A[i, j] - A[i - 1, j] <= 1:
				C[i, j] |= 1
			if i < N - 1 and A[i, j] - A[i + 1, j] <= 1:
				C[i, j] |= 2
			if j > 0 and A[i, j] - A[i, j - 1] <= 1:
				C[i, j] |= 4
			if j < N - 1 and A[i, j] - A[i, j + 1] <= 1:
				C[i, j] |= 8
	Q = Queue()
	Q.put((0, 0))
	visited = set([(0, 0)])
	while not Q.empty():
		x, y = Q.get()
		for i, j in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
			if 0 <= x + i < N and 0 <= y + j < N and (C[x + i, y + j] & (C[x, y] >> (2 * i + j))):
				Q.put((x + i, y + j))
				visited.add((x + i, y + j))
	return max([math.sqrt((X - 0) ** 2 + (Y - 0) ** 2) for (X, Y) in visited])

A = np.array([[2001, 1000, 100], [1001, 10000, 200], [100, 0, 0]])
print(solve(A, 0))
