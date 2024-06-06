
from math import *
R,x1,y1,x2,y2 = map(int,input().split())
dis = sqrt((x1-x2)**2 + (y1-y2)**2)

if dis<R:
    x_ap,y_ap = x1,y1
    r = dis
    print(x_ap,y_ap,r)
else:
    x_ap,y_ap = x1,y1
    r = R - dis + R
    print(x_ap,y_ap,r)
