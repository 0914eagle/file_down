
a=list(map(int,input().split()))
l=[]
m=[]
for i in range(a[0]):
    b=list(map(int,input().split()))
    l.append(b)
for i in range(len(l)):
    m.append(l[i][1])
print(l[len(l)-1][0]+sum(m),sum(m)+len(m))
