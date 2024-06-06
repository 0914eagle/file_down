

for _ in range(int(input())):
    x,y = map(int,input().split())
    a,b = map(int,input().split())
    #print(x,y)
    if x == 0 and y == 0:
        print(0)
    else:
        if x == 0:
            if (y%2 == 0):
                print(y//2*b)
            else:
                print(b+y//2*b)
        elif y == 0:
            if (x%2 == 0):
                print(x//2*a)
            else:
                print(a+x//2*a)
        else:
            if x == y:
                print(a*x)
            else:
                d = abs(x-y)
                if (d%2 == 0):
                    print(d//2*a+d//2*b)
                else:
                    print(d//2*a+d//2*b+a)
        
