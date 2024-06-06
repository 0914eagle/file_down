
f,i,t=map(int,input().split())
a=[]
for _ in range(f):
    a.append(input())
c=0
for j in range(i):
    s=0
    for k in range(f):
        if a[k][j]=='Y':
            s+=1
    if s>=t:
        c+=1
print(c)
