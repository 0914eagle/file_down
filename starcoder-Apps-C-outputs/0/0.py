
x,y = map(int,input().split())
v,w = map(float,input().split())
import math
if x != 0:
    l = math.sqrt(x**2+y**2)
    a = math.acos(abs(x)/l)
    if x < 0:
        a = -a
    if y < 0:
        a = math.pi*2 - a
    t = l/v
    if (a*w)%(math.pi*2) > math.pi:
        t = t + (math.pi*2-abs(a*w))/(w)
    else:
        t = t + abs(a*w)/w
else:
    if y > 0:
        t = y/v
    else:
        t = 0
print(t)
