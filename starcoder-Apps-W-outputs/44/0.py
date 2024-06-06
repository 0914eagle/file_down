
n,m=map(int,input().split())
f=list(map(int,input().split()))
b=list(map(int,input().split()))
c=0
g=[]
h=[]
for i in range(n):
    for j in range(m):
        if b[j]==f[i]:
            g.append(i+1)
            h.append(b[j])
            c+=1
            break
if c==m:
    print("Possible")
    for i in range(m):
        print(g[i],end=" ")
else:
    print("Impossible")

