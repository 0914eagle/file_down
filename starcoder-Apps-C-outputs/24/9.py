
n=int(input())
m=[]
for i in range(n):
    a=list(input())
    m.append(a)
for i in range(n):
    for j in range(n):
        if m[i][j]=='E':
            m[i][j]=1
        else:
            m[i][j]=0
for i in range(n):
    for j in range(n):
        if m[i][j]==1:
            for k in range(n):
                m[k][j]=1
                m[i][k]=1
s=[]
for i in range(n):
    for j in range(n):
        if m[i][j]==0:
            s.append((i+1,j+1))
if len(s)==0:
    print(-1)
else:
    for i in s:
        print(i[0],i[1])
