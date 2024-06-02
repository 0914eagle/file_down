
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def check(x):
    cnt = 0
    for i in range(x):
        if A[N-1-i] + B[M-1-i] <= K:
            cnt += 1
    return cnt

ok = 0
ng = min(N, M) + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid) >= mid:
        ok = mid
    else:
        ng = mid

print(ok)

