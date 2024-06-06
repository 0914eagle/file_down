
import math
R,x_1,y_1,x_2,y_2=map(float,input().split())
r_1=math.sqrt((x_1-x_2)**2+(y_1-y_2)**2)
r_2=R-r_1
x_ap=x_1
y_ap=y_1
if r_2<R:
    print("{:.10f} {:.10f} {:.10f}".format(x_ap,y_ap,r_2))
else:
    print("{:.10f} {:.10f} {:.10f}".format(x_1,y_1,R))
