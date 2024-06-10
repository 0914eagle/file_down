
N = int(input())
A = list(map(int, input().split()))

s1 = 0
s2 = 0

for i in range(N):
  s1 += abs(A[i])
  s2 += abs(A[i] - A[i-1])

for i in range(N):
  print(s1 - s2 + abs(A[i-1]) + abs(A[i+1] - A[i-1]))

