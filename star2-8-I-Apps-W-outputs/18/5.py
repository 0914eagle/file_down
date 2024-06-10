
n, a, b = map(int, input().split())
h = [int(input()) for _ in range(n)]

def count_explosion(h):
    return sum(hi - b > 0 for hi in h)

lb, ub = 0, n
while ub - lb > 1:
    m = (lb + ub) // 2
    if count_explosion(h) <= m:
        ub = m
    else:
        lb = m
print(ub)

