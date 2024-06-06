
import math

x,y=map(int,input().split())
v,w=map(float,input().split())
x=abs(x)
y=abs(y)
t=0
if x==0 and y==0:
    print(0)
else:
    l=math.sqrt(x*x+y*y)
    if x==0:
        w=math.pi
    elif y==0:
        w=0
    else:
        w=math.atan(x/y)
    if w<0:
        w=w+math.pi*2
    a=(w/(math.pi/2))
    t1=math.pi/w
    t2=l/v
    t3=(math.pi-w)/(math.pi/2)
    t=t1+t2+t3
    print(t)
