
n,m = map(int,input().split())
l = list(map(int,input().split()))
ans = 0
for i in range(n):
    a = l[i]
    if a&1==0:
        ans+=m-a+1
    else:
        ans+=m-a
    if (a+1)&1==0 and (a+1)<=m:
        ans+=m-(a+1)//2+1
    else:
        ans+=m-(a+1)//2
for i in range(n):
    for j in range(i+1,n):
        a,b = l[i],l[j]
        if a&1==0 and b&1==0:
            if a>b:
                a,b=b,a
            if b<m-a+1:
                ans+=b
            else:
                ans+=m-a+1
        elif a&1==0 and b&1:
            if a>b+1:
                a,b=b,a
            if b+1<m-a+1:
                ans+=b+1
            else:
                ans+=m-a+1
        elif a&1 and b&1==0:
            if a+1>b:
                a,b=b,a
            if b<m-(a+1)//2+1:
                ans+=b
            else:
                ans+=m-(a+1)//2+1
        elif a&1 and b&1:
            if a+1>b+1:
                a,b=b,a
            if b+1<m-(a+1)//2+1:
                ans+=b+1
            else:
                ans+=m-(a+1)//2+1
print(ans)
