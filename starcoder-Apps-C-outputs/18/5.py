
n,k = map(int,input().split())
c = list(map(int,input().split()))
c.sort()
print(c)
q=[]
for i in range(n):
    for j in range(n):
        if c[i]+c[j]==k:
            q.append(c[i])
            q.append(c[j])
q = list(set(q))
q.sort()
print(len(q))
print(*q)
