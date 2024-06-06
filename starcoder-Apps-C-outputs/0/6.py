
import math

x, y = list(map(int, input().split()))
v, w = list(map(float, input().split()))

print(min(v/w*math.pi, (abs(x)+abs(y))/v, (abs(x)+abs(y))/v+abs(x)*w/v, (abs(x)+abs(y))/v+abs(y)*w/v))
