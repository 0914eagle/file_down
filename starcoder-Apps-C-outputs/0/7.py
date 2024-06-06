
import math
x,y = map(int,input().split())
v,w = map(float,input().split())
if x == 0 and y != 0:
    print(abs(y/v))
elif y == 0 and x != 0:
    print(abs(x/v))
else:
    print(abs((math.sqrt(x**2+y**2)+x)/v))
