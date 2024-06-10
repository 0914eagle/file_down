
N, A, B = map(int, input().split())
H = [int(input()) for i in range(N)]

def can_vanish(n_explosion):
    vanished = 0
    for h in H:
        if h <= A * n_explosion:
            vanished += 1
        elif h - B * n_explosion > 0:
            vanished += (h - B * n_explosion + A - B - 1) // (A - B)
    return vanished >= N

ok = 0
ng = 10**9 + 1
while abs(ok - ng) > 1:
    mid = (ok + ng) // 2
    if can_vanish(mid):
        ok = mid
    else:
        ng = mid
print(ok)

