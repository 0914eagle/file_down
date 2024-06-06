
import math
x,y = map(int,input().split())
v,w = map(float,input().split())
if x==0 and y==0:
    print(0)
elif x == 0:
    print(abs(y)/v)
elif y == 0:
    print(abs(x)/v)
else:
    print(math.sqrt(x*x+y*y)/v+math.atan(y/x)/w)
