
n,m=map(int,input().split())
if n==1 and m!=1:
    print("Impossible")
elif n==1:
    print("1")
elif m==1:
    print("1"*n)
else:
    a=int("1"+"0"*(n-1))
    a*=m
    if len(str(a))==n:
        print(a)
    else:
        print("Impossible")
