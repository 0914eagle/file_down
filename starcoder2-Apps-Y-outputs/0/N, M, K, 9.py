
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

ans = 0

for i in range(N):
    if K - A[i] < 0:
        break
    K -= A[i]
    ans += 1

for i in range(M):
    if K - B[i] < 0:
        break
    K -= B[i]
    ans += 1

print(ans)

