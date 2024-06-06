
from sys import stdin
from sys import stdout
from collections import deque
n = int(stdin.readline().strip())
ans = 0
d = {}
q = deque()
for i in range(n):
    tmp = stdin.readline().strip().split()
    p = int(tmp[0])
    d[i] = []
    for j in range(p):
        t = stdin.readline().strip().split()
        if j == 0:
            ans += int(t[0])
        else:
            d[i].append(int(t[2]))
for k,v in d.items():
    for e in v:
        d[e].append(k)
for k,v in d.items():
    if k not in v:
        q.append(k)
while len(q) > 0:
    n = q.popleft()
    for e in d[n]:
        if e != n:
            d[e].remove(n)
            if e not in d[e]:
                q.append(e)
ans += n-len(q)
stdout.write(str(ans))
