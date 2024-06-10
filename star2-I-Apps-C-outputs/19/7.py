
def solve(n, C, ps, bs, us):
    return 0

n, C = map(int, input().split())
ps = [0] * n
bs = [0] * n
us = [0] * n
for i in range(n):
    ps[i], bs[i], us[i] = map(int, input().split())

print(solve(n, C, ps, bs, us))

