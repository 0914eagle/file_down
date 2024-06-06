

# -*- coding: utf-8 -*-


import math

def shoot(r, x, y, t, hit):
    hit.append(math.sqrt((x+r*math.cos(t))**2+(y+r*math.sin(t))**2))

n = int(input())
x = []
y = []
r = []
for i in range(n):
    inp = input().split()
    x.append(float(inp[0]))
    y.append(float(inp[1]))
    r.append(float(inp[2]))

hit = []
for i in range(n):
    shoot(r[i], x[i], y[i], 0, hit)
    shoot(r[i], x[i], y[i], math.pi, hit)

hit.sort()
count = 0
prev = -1
for i in range(len(hit)):
    if(prev != hit[i]):
        count += 1
    prev = hit[i]

print(int(count/2))

