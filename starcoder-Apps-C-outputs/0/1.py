
import math
x,y = input().split()
x,y = float(x),float(y)
v,w = input().split()
v,w = float(v),float(w)

r = x**2+y**2
r = math.sqrt(r)

t1 = r/v
t2 = (2*math.pi)/w

if t1>t2:
    print(t1)
else:
    print(t2)
