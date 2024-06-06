

n,x,k=list(map(int,input().split()))
a=list(map(int,input().split()))
l=[]
c=0
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if a[i]<=a[j] and a[i]%x<=k<=a[j]%x:
            l.append((i,j))
print(len(l))

