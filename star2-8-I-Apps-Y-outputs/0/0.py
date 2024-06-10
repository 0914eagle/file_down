
def solve(s):
    n = len(s)
    p = [0] * n # prefix
    q = [0] * n # suffix
    for i in range(n):
        if s[i] == 'L':
            p[i] += 1
        elif s[i] == 'R':
            p[i] -= 1
        elif s[i] == 'U':
            p[i] += 1j
        elif s[i] == 'D':
            p[i] -= 1j
    for i in range(n - 1, -1, -1):
        if s[i] == 'L':
            q[i] += 1
        elif s[i] == 'R':
            q[i] -= 1
        elif s[i] == 'U':
            q[i] += 1j
        elif s[i] == 'D':
            q[i] -= 1j
    for i in range(n - 1):
        p[i + 1] += p[i]
    for i in range(n - 1, 0, -1):
        q[i - 1] += q[i]
    res = (0, 0)
    for i in range(n):
        if p[i] == q[i]:
            res = (i + 1, i + 1)
    for i in range(n - 1):
        if p[i] == q[i + 1]:
            res = (i + 1, i + 2)
    if res == (0, 0):
        print(-1)
    else:
        print(*res)

t = int(input())
for _ in range(t):
    n = int(input())
    s = input()
    solve(s)

