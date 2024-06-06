
for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    if x==y==0:
        print(0)
    elif x==y:
        print(a*x)
    elif x==0 or y==0:
        print(min(x*a,y*a))
    else:
        print(min(x*a+y*a,b*(x+y)))
