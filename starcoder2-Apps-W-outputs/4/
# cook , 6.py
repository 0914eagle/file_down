
# cook your dish here
f,i,t=map(int,input().split())
l=[]
for _ in range(f):
    l.append(input())
c=0
for j in range(i):
    s=0
    for k in range(f):
        if l[k][j]=='Y':
            s+=1
    if s>=t:
        c+=1
print(c)
