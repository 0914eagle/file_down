
n,m,x,y=map(int,input().split())
s=input()
l=len(s)
a=[0]*(l+1)
a[0]=1
for i in range(l):
    if s[i]=='U':
        x-=1
    elif s[i]=='D':
        x+=1
    elif s[i]=='L':
        y-=1
    else:
        y+=1
    if x<1 or x>n or y<1 or y>m:
        continue
    a[i+1]=a[i]
for i in range(l+1):
    print(a[i],end=' ')
