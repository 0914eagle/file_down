
n=int(input())
if n==0:
    print('-1')
else:
    a=list(map(int,input().split()))
    c=[i for i in range(1,10)]
    b=[]
    for i in range(len(c)):
        b.append(a[i])
        a[i]=b[i]
    a=sorted(a,reverse=True)
    print(a)
    p=1
    for i in range(len(a)):
        print(p,end='')
        if a[i]*p<=n:
            n-=a[i]*p
        else:
            print(n//a[i])
            p+=1
