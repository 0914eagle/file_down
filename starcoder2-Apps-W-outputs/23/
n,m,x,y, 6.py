
n,m,x,y=map(int,input().split())
s=input()
a=[0]*(len(s)+1)
a[0]=1
for i in range(len(s)):
    if s[i]=='U':
        x-=1
    elif s[i]=='D':
        x+=1
    elif s[i]=='L':
        y-=1
    else:
        y+=1
    a[i+1]=a[i]
    if x<1 or x>n or y<1 or y>m:
        a[i+1]=0
print(*a)
