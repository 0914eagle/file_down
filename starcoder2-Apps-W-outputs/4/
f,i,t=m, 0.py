
f,i,t=map(int,input().split())
l=[]
for _ in range(f):
    l.append(input())
c=0
for j in range(i):
    count=0
    for k in range(f):
        if l[k][j]=='Y':
            count+=1
    if count>=t:
        c+=1
print(c)
