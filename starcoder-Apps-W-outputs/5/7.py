
n,m=map(int,input().split())
a=[]
for i in range(m):
    a.append(list(map(int,input().split())))
if len(a)==1:
    print(n-m)
    for i in range(1,n+1):
        if i!=a[0][0] and i!=a[0][1]:
            print(i)
else:
    b=[0]*(n+1)
    for i in range(m):
        if b[a[i][0]]==0:
            b[a[i][0]]=1
            b[a[i][1]]=1
        elif b[a[i][1]]==0:
            b[a[i][1]]=1
    if b.count(0)==0:
        print("Connected")
    else:
        print(b.count(0)-1)
        for i in range(1,n+1):
            if b[i]==0:
                print(i)
