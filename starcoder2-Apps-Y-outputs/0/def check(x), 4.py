
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def check(x):
    cnt = 0
    i = 0
    j = 0
    while i < N and j < M:
        if A[i] + B[j] <= x:
            cnt += 1
            i += 1
            j += 1
        elif A[i] < B[j]:
            i += 1
        else:
            j += 1
    cnt += min(N - i, M - j)
    return cnt

ok = -1
ng = K + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid) >= (N + M) // 2:
        ok = mid
    else:
        ng = mid
print(ok)

