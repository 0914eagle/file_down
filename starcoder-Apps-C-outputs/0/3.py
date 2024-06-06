
x,y=map(int,input().split())
v,w=map(float,input().split())
import math
d=math.sqrt(x*x+y*y)
w=v/w
if x==0:
    if y>0:
        print(d/v)
    else:
        print((w*math.pi+d)/v)
elif y==0:
    if x>0:
        print(d/v)
    else:
        print((w*math.pi+d)/v)
elif x>0 and y>0:
    print((math.atan(y/x)*w+d)/v)
elif x>0 and y<0:
    print((math.pi+math.atan(abs(y/x))*w+d)/v)
elif x<0 and y<0:
    print((math.pi*2+math.atan(abs(y/x))*w+d)/v)
elif x<0 and y>0:
    print((math.pi+math.atan(abs(y/x))*w+d)/v)

