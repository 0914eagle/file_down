
a,b=map(int,input().split())
x=[]
for i in range(a):
    x.append(input())
c=1
d=1
for i in range(a):
    if(x[i]=='half'):
        c+=1
    else:
        d+=1
print((c*d*b)//2)
