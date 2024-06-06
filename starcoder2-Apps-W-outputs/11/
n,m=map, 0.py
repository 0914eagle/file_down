
n,m=map(int,input().split())
a=list(map(int,input().split()))
l=[]
for i in range(m):
    l.append(list(map(int,input().split())))
s=0
for i in range(m):
    for j in range(l[i][0]-1,l[i][1]):
        s+=a[j]
print(s)
