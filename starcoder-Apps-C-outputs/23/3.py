
from math import *
import numpy as np
from queue import PriorityQueue

a,m = map(float,input().split())
W,H,X,Y = map(int,input().split())

h = np.zeros((H,W))

for i in range(H):
    h[i] = np.array(list(map(int,input().split())))

q = PriorityQueue()
q.put((0,X,Y))
used = [[0]*W for i in range(H)]
ans = 0
used[X][Y] = 1
while not q.empty():
    dist,x,y = q.get()
    #print(x,y,dist)
    ans = max(ans,dist)
    for dx,dy in [(0,-1),(0,1),(1,0),(-1,0)]:
        nx = x+dx
        ny = y+dy
        if nx < 0 or ny < 0 or nx >= W or ny >= H or used[nx][ny]:
            continue
        v = 0.5*a*(np.cos(dist/12*pi)+1)
        if abs(h[nx][ny]-h[x][y]) > 1:
            continue
        if abs(h[nx][ny]-v) <= m:
            used[nx][ny] = 1
            q.put((dist,nx,ny))
        if abs(h[x][y]-v) <= m:
            used[nx][ny] = 1
            q.put((dist+1,nx,ny))

print(round(ans*10,2))
