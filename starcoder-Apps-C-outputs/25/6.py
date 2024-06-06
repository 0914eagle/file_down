
import sys
sys.setrecursionlimit(100000)
def findmax(k):
    if k in mem:
        return mem[k]
    res = 1
    for i in a[k]:
        res = max(res,findmax(i)+1)
    mem[k] = res
    return mem[k]
def add(x,y):
    for i in range(n):
        if a[i][x]==a[i][y]:
            a[i].remove(y)
    a[y].remove(x)
    a[x].append(y)
n,m = map(int,input().split())
a = [[] for i in range(n)]
b = []
for i in range(n):
    x,y = map(int,input().split())
    b.append((x,y))
for i in range(n):
    x,y = b[i]
    for j in range(n):
        if i==j:
            continue
        xx,yy = b[j]
        if xx>=x and xx<=x+9 and yy>=y and yy<=y+14:
            add(i,j)
mem = {}
print(max(map(findmax,range(n))))
