
from math import sqrt
def dist(a,b):
  return sqrt((a[0]-b[0])**2+(a[1]-b[1])**2)
def dist_t(a,b,t):
  return sqrt((a[0]-b[0]+t*v[0])**2+(a[1]-b[1]+t*v[1])**2)
x1,y1,x2,y2=map(int,input().split())
vmax,t=map(int,input().split())
v_x,v_y=map(int,input().split())
w_x,w_y=map(int,input().split())
a=dist((x1,y1),(x2,y2))
if dist((x1,y1),(x2,y2))<vmax:
  print(dist((x1,y1),(x2,y2)))
else:
  v=(v_x,v_y)
  w=(w_x,w_y)
  d=dist((x1,y1),(x2,y2))
  t1=d/vmax
  d1=dist_t((x1,y1),(x2,y2),t1)
  t2=(d-d1)/vmax
  d2=dist_t((x1,y1),(x2,y2),t2)
  print(t1+t2+d2)

