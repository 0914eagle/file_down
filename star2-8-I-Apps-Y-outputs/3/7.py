
N,L = map(int,input().split())

A = [0] * N
for i in range(N):
  A[i] = L + i

max_A = max(A)
min_A = min(A)

A.remove(max_A)
A.remove(min_A)

print(sum(A))


