
n=int(input())
a=list(map(int,input().split()))
b=[]
c=[]
d=[]
e=[]
for i in range(n):
    if a[i]%4==0:
        b.append(i+1)
    elif a[i]%4==1:
        c.append(i+1)
    elif a[i]%4==2:
        d.append(i+1)
    elif a[i]%4==3:
        e.append(i+1)
if len(b)<len(c) or len(b)<len(d) or len(b)<len(e):
    print('No')
elif len(c) == 0 and len(e) == 0 and len(d) < 2:
    print('No')
else:
    print('Yes')
    ans = []
    for i in range(len(c)):
        ans.append(c[i])
        ans.append(b[i])
        ans.append(d[i])
        ans.append(e[i])
    if len(d) > len(e):
        for i in range(len(e),len(d)):
            ans.append(b[i])
            ans.append(d[i])
    elif len(d) < len(e):
        for i in range(len(d),len(e)):
            ans.append(b[i])
            ans.append(e[i])
    print(' '.join(map(str,ans)))
