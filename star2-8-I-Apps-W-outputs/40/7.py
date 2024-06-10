
n,m = map(int, input().split())
l = [[] for i in range(n+1)]
for i in range(m):
  a,b = map(int, input().split())
  l[a].append(b)
  l[b].append(a)

for i in range(1,n+1):
  if len(l[i]) == n-1:
    print("YES")
    exit()
    
print("NO")

