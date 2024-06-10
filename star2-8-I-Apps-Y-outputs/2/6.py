
N = int(input())
A = list(map(int, input().split()))
A.sort()

diff = []
for i in range(N - 1):
  diff.append(A[i + 1] - A[i])

print(sum(diff) + max(diff))

