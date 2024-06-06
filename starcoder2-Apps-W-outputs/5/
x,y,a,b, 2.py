
x,y,a,b = map(int,input().split())
if x-a > y-b:
    print(0)
else:
    print(y-b+1)
    for i in range(b,y+1):
        print(x,i)
