
import sys

n,m = map(int, input().split())
p,r = map(int, input().split()), map(int, input().split())
c = [0]*n
t = [0]*n
for i in range(n):
    c[i],t[i] = map(int, input().split())

p.sort()
r.sort()

ans = 0
pc = [0]*(m+1)
rc = [0]*(m+1)
for i in range(n):
    idx = c[i]-1
    if pc[idx] == 0 and rc[idx] == 0:
        ans += 1
        pc[idx] = 1
        rc[idx] = 1
    elif rc[idx] == 0:
        ans += 1
        rc[idx] = 1
    elif pc[idx] == 0:
        ans += 1
        pc[idx] = 1
print(ans)
