
n,m = map(int,input().split())
l = [0 for i in range(n+1)]
for i in range(m):
    a,b = map(int,input().split())
    l[a] += 1
    l[b] += 1
if max(l) >= 2:
    print("YES")
else:
    print("NO")

