
n,m=list(map(int,input().split()))
l=[]
for i in range(m):
    k=list(map(int,input().split()))
    l.append(k[1:])
t=list(map(int,input().split()))
k=[]
for i in range(len(l)):
    for j in range(len(l[i])):
        k.append(l[i][j])
v=[]
for i in range(len(t)):
    if t[i]!=0:
        v.append(i+1)
u=[]
for i in range(len(v)):
    if v[i] in k:
        u.append(v[i])
for i in range(len(u)):
    if t[u[i]-1]==0:
        t[u[i]-1]=1
    else:
        t[u[i]-1]=0
print(t)
if t==[1]*n:
    print('YES')
else:
    print('NO')
