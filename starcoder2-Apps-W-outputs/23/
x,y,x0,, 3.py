
x,y,x0,y0=map(int,input().split())
s=input()
n=len(s)
a=[0]*(n+1)
a[0]=1
for i in range(n):
    if s[i]=='L':
        y0-=1
    elif s[i]=='R':
        y0+=1
    elif s[i]=='U':
        x0-=1
    else:
        x0+=1
    if x0<1 or x0>x or y0<1 or y0>y:
        a[i+1]=a[i]
    else:
        a[i+1]=a[i]+1
print(*a)
