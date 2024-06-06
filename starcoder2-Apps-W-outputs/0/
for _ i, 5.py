
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x==y==0:
        print(0)
    elif x==y:
        print(x*a)
    elif x>y:
        print(y*a+(x-y)*b)
    else:
        print(x*a+(y-x)*b)
