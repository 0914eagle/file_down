
n,l=map(int,input().split())
a=list(map(int,input().split()))
c=list(map(int,input().split()))
a.sort()
c.sort()
x=y=l
ans=1e9
for i in range(n-l+1):
    x+=a[i]
    y-=a[i]
    ans=min(ans,(c[i]/x)*(sum(c)/y))
print("{:.3f}".format(ans))

