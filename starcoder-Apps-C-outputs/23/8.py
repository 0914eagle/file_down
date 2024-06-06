
import math

def check(x, y, z):
    if x >= z:
        return True
    if y >= z:
        return True
    if x+y >= z:
        return True
    return False

def check_time(time, x, y, z):
    if time == 0:
        return check(x, y, z)
    return True

def get_height(time, a):
    return 0.5*a*(math.cos(time*math.pi/6.0) + 1.0)

def go(x, y, h):
    global data, m, n, t, x0, y0, dist
    if check_time(t, x, y, h) == False:
        return
    if data[x][y] != 0:
        return
    data[x][y] = 1
    #print(x, y, dist, time, h)
    dist = max(dist, math.sqrt(x**2 + y**2))
    if x > 0:
        go(x-1, y, get_height(t, a))
    if x < m-1:
        go(x+1, y, get_height(t, a))
    if y > 0:
        go(x, y-1, get_height(t, a))
    if y < n-1:
        go(x, y+1, get_height(t, a))
    data[x][y] = 0

a, m = list(map(float, input().split()))
m = m/1000.0
m, n, x0, y0 = list(map(int, input().split()))
data = [[] for i in range(m)]
for i in range(m):
    data[i] = list(map(int, input().split()))
dist = 0
t = 0.0
go(x0, y0, get_height(t, a))
t = 12.0
go(x0, y0, get_height(t, a))
print(dist)

