
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    k=1
    a=l[0]
    for i in range(1,n):
        if(l[i]!=l[i-1]):
            k+=1
        if(a<l[i]):
            a=l[i]
    print(a,k)
