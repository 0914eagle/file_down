
x,y,a,b = map(int,input().split())
if x>a and y>b:
    if x-a>y-b:
        print(1)
        print(x,y)
    elif x-a<y-b:
        print(1)
        print(x,y)
    else:
        print(2)
        print(x,y)
        print(x-1,y-1)
else:
    print(0)
