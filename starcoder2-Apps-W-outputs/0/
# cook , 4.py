
# cook your dish here
for _ in range(int(input())):
    x,y=map(int,input().split())
    a,b=map(int,input().split())
    if x==y==0:
        print(0)
    else:
        print(min(a*abs(x-y),b*abs(x-y)+a*abs(x-y)))
