
x,y,a,b=map(int,input().split())
if a>x or b>y:
    print(0)
else:
    print(x-a+1)
    for i in range(a,x+1):
        print(i,y-i+b)
