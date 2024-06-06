
s,b=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
d=[]
g=[]
for i in range(b):
    x,y=map(int,input().split())
    d.append(x)
    g.append(y)
d.sort()
c=0
maxi=0
count=0
for i in a:
    maxi=max(maxi,i)
    while count<b and d[count]<=maxi:
        c+=g[count]
        count+=1
    print(c,end=" ")
