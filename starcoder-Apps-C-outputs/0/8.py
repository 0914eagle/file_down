
import math

def get(x,y,v,w):
    x,y = abs(x),abs(y)
    if x == y:
        return 2*math.pi*x/w
    if x < y:
        x,y = y,x
    return v*math.sqrt(2)*math.sqrt(2*x*x - x*x + y*y)/(v*v + w*w)

while True:
    try:
        x,y,v,w = map(eval,input().split())
        print(get(x,y,v,w))
    except:
        break
