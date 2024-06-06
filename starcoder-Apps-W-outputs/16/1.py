
import math as m
r,x,y,a,b=map(int,input().split())
if r>m.sqrt((x-a)**2+(y-b)**2):
    print("%.10f %.10f %.10f"%(x,y,r))
elif m.sqrt((x-a)**2+(y-b)**2)>r:
    r=m.sqrt((x-a)**2+(y-b)**2)
    print("%.10f %.10f %.10f"%(a,b,r))
else:
    r=m.sqrt((x-a)**2+(y-b)**2)
    print("%.10f %.10f %.10f"%(x,y,r))
