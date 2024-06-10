
def solve(n, a):
    if n == 1:
        return -1
    if a[0] < 0 or a[-1] > 0:
        return -1
    stack = []
    for i in range(n):
        if a[i] > 0:
            if a[i] in stack:
                return -1
            stack.append(a[i])
        else:
            if -a[i] not in stack:
                return -1
            stack.remove(-a[i])
    if len(stack) != 0:
        return -1
    d = 1
    c = [0] * d
    for i in range(n):
        if a[i] > 0:
            c[d - 1] += 1
        else:
            if c[d - 1] == 0:
                d += 1
                c.append(0)
            c[d - 1] += 1
    return d, c

n = int(input())
a = list(map(int, input().split()))
res = solve(n, a)
if res == -1:
    print(res)
else:
    print(res[0])
    print(' '.join(map(str, res[1])))

