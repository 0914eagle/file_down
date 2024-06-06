
n,m = map(int,input().split())
a = list(map(int,input().split()))
d = [[] for i in range(n)]
for i in range(m):
    x,y = map(int,input().split())
    d[x].append(y)
ans = 0
for i in range(n):
    if a[i] == 0:
        continue
    ans += 1
    for j in d[i]:
        a[j] = 0
print(ans)
