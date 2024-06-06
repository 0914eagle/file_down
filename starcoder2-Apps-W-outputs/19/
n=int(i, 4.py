
n=int(input())
l=[]
for i in range(n):
    x,y=map(int,input().split())
    l.append((x,y))
l.sort()
c=0
for i in range(n):
    if i==n-1:
        break
    if l[i][0]==l[i+1][0]:
        c+=1
    else:
        break
if c==n-1:
    print(1)
else:
    l.sort(key=lambda x:x[1])
    c=0
    for i in range(n):
        if i==n-1:
            break
        if l[i][1]==l[i+1][1]:
            c+=1
        else:
            break
    if c==n-1:
        print(1)
    else:
        print(2)
