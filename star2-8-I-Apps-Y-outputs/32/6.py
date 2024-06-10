
n, k = map(int, input().split())

r = list(map(int, input().split()))

q = [list(map(int, input().split())) for i in range(k)]

q.sort(key=lambda x: (x[0], x[1]))

q = [x for x in q if x[0] < x[1]]

can_be_mentor = [0] * n

for i in range(n):
    l, r = i - 1, i
    while l >= 0 and r < n:
        if (l >= 0 and q[l][0] == i and q[l][1] == r):
            l -= 1
            continue
        if (r < n and q[r][0] == i and q[r][1] == l):
            r += 1
            continue
        if (l >= 0 and r < n and q[l][0] == i and q[l][1] == r):
            l -= 1
            r += 1
            continue
        if (r < n and q[r][0] == i and q[r][1] == l):
            l -= 1
            r += 1
            continue
        if (l >= 0 and q[l][0] == i and q[l][1] == i):
            l -= 1
            continue
        if (r < n and q[r][0] == i and q[r][1] == i):
            r += 1
            continue
        if (l >= 0 and q[l][0] == r and q[l][1] == i):
            l -= 1
            continue
        if (r < n and q[r][0] == l and q[r][1] == i):
            r += 1
            continue
        can_be_mentor[i] += r - l - 1
        break

print(*can_be_mentor)

