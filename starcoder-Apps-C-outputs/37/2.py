
n,m=map(int,input().split())
a=sorted([[int(i) for i in input().split()] for j in range(m)])
for i in range(m):
    if i%2==0:
        if a[i][1]<=n-2:
            print('impossible')
            break
    else:
        if a[i][1]<=n:
            print('impossible')
            break
else:
    ans=''
    i=0
    while n:
        n-=1
        if i%2==0:
            ans+='0'
            if a[i][1]-1<=n:
                ans+='+'*n
            else:
                ans+='+'*(a[i][1]-1)
            n-=a[i][1]-1
        else:
            ans+='-'
            if a[i][1]-2<=n:
                ans+='+'*n
            else:
                ans+='+'*(a[i][1]-2)
            n-=a[i][1]-2
        i+=1
    print(ans)
