
N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
A.sort()
B.sort()

def check(x):
    a = 0
    b = 0
    for i in range(x):
        if A[N-i-1] > B[M-i-1]:
            a += A[N-i-1]
        else:
            b += B[M-i-1]
    return a + b <= K

ok = 0
ng = N + 1
while ng - ok > 1:
    mid = (ok + ng) // 2
    if check(mid):
        ok = mid
    else:
        ng = mid
print(ok)

