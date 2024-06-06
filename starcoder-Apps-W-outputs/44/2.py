
n,m=map(int,input().split())
f=list(map(int,input().split()))
b=list(map(int,input().split()))
s1=set()
s2=set()
res=[]
for i in range(n):
    s1.add(f[i])
for i in range(m):
    s2.add(b[i])
if len(s1)==len(s2)==n:
    print("Possible")
    for i in range(m):
        print(f.index(b[i])+1,end=" ")
else:
    print("Impossible")
