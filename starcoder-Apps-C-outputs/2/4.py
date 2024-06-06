
n,d,c=map(int,input().split())
l1=list(map(int,input().split()))
l2=list(map(int,input().split()))
if(d==1):
    print(n)
else:
    p=(n-c)/(n-c+d-1)
    p=p**c
    print(1/p)
