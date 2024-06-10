
N = int(input())
A = list(map(int, input().split()))

dist = [0] * (N + 1)
for i in range(1, N + 1):
    dist[i] = dist[i-1] + abs(A[i-1] - A[i])

for i in range(1, N + 1):
    print(dist[i-1] + dist[N] - dist[i] + abs(A[i-1]))

