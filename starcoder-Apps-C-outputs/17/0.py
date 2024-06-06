
def solve():
    N, M = map(int, input().split())
    c = []
    for _ in range(N):
        c.append(list(map(int, input().split())))
    r = [0]*M
    for i in range(M):
        r[i] = -1
        f = c[0][i+4]
        if f == 0:
            continue
        d1 = c[0][0]
        m1 = c[0][1]
        d2 = c[0][2]
        m2 = c[0][3]
        for j in range(1, N):
            if c[j][4+i] != f:
                continue
            if c[j][0] != d1 or c[j][1] != m1 or c[j][2] != d2 or c[j][3] != m2:
                continue
        r[i] = (m2 - m1) * 30 + (d2 - d1)
        if (r[i] + d1 + 30*m1) % 365 != d2 + 30*m2 % 365:
            r[i] = -1
    if r == [-1]*M:
        return '-1'
    return ' '.join(map(str, r))

print(solve())
