
# cook your dish here
x,y,a,b=map(int,input().split())

if x-a+y-b>0:
    print(0)
else:
    print(1)
    print(a,b)
