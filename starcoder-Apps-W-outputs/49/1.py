
for _ in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    b=[]
    for i in range(n):
        if i==0:
            b.append("a"*(a[i]+1))
        else:
            b.append("b"*(a[i]-a[i-1]+1))
    print(*b,sep="\n")
