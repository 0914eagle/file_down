
# TLE
def snap(p, i, j, w):
    while p[i][w] > p[j][w]:
        i += 1
    while p[i][w] < p[j][w]:
        j -= 1
    if i == j:
        return p[:i] + p[i+1:]
    return p[:i] + p[i+1:j] + p[j+1:]
def solve(p):
    if len(p) == 2:
        return [[1, 2]]
    p_x = sorted(p, key=lambda p: p[0])
    p_y = sorted(p, key=lambda p: p[1])
    p_z = sorted(p, key=lambda p: p[2])
    n = len(p)
    s = []
    s += solve(snap(p_x, 0, n-1, 0))
    s += solve(snap(p_y, 0, n-1, 1))
    s += solve(snap(p_z, 0, n-1, 2))
    return s

# AC
def solve(p):
    if len(p) == 2:
        return [[1, 2]]
    p_x = sorted(p, key=lambda p: p[0])
    p_y = sorted(p, key=lambda p: p[1])
    p_z = sorted(p, key=lambda p: p[2])
    n = len(p)
    s = []
    s += solve(snap(p_x, 0, n-1, 0))
    s += solve(snap(p_z, 0, n-1, 2))
    s += solve(snap(p_y, 0, n-1, 1))
    return s
