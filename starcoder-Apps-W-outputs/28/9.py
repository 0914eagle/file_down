

for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x==0 and y==0:
        print(0)
    else:
        print(min(abs(x-y)*a,abs(x-y)*b))
