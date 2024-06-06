
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x==y==0:
        print(0)
    else:
        print(min(x*a+y*a,x*b+y*b,x*a+y*b,x*b+y*a))
