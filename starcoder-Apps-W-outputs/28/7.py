
T = int(input())
while T>0:
    T-=1
    x, y = [int(i) for i in input().split()]
    a, b = [int(i) for i in input().split()]
    if x==y:
        print(0)
    else:
        print(min(abs(x-y)*a, abs(x-y)*b))
