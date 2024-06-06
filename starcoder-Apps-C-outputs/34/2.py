
h,t=map(int,input().split())
x,y=h,t
for i in range(int(input())-1):
    h,t=map(int,input().split())
    if h>x:
        x=h
    if t>y:
        y=t
print(x*y)
