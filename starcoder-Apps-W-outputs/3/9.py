
n,k,q=map(int,input().split())
l=[0]*200001
r=[0]*200001
for i in range(n):
    a,b=map(int,input().split())
    l[a]+=1
    r[b+1]-=1
for i in range(1,200001):
    l[i]=l[i-1]+l[i]
for i in range(200000,-1,-1):
    r[i]=r[i+1]+r[i]
for i in range(1,200001):
    l[i]=l[i-1]+r[i]
for i in range(q):
    a,b=map(int,input().split())
    print(l[b]-l[a-1])
