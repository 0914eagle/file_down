
import math
def minr(R,x1,y1,x2,y2):
    dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return (dis+R)/2
def maxr(R,x1,y1,x2,y2):
    dis=math.sqrt((x1-x2)**2+(y1-y2)**2)
    return (dis+R)
R,x1,y1,x2,y2=map(int,input().split())
r1=minr(R,x1,y1,x2,y2)
r2=maxr(R,x1,y1,x2,y2)
x=(x1*r2-x2*r1)/(r2-r1)
y=(y1*r2-y2*r1)/(r2-r1)
print(x,y,r1)
