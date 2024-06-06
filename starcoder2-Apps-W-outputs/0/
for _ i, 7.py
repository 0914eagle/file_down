
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x==y==0:
        print(0)
    elif x==0 or y==0:
        print(min(a,b))
    else:
        print(min(a+b,2*min(a,b)))
