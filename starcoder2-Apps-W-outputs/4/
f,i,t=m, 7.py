
f,i,t=map(int,input().split())
l=[]
for _ in range(f):
    l.append(input())
c=0
for j in range(i):
    k=0
    for m in l:
        if m[j]=='Y':
            k+=1
    if k>=t:
        c+=1
print(c)
