
from sys import stdin
from math import pi, cos, sin

n = int(input())
opponents = [[float(x) for x in stdin.readline().strip().split(' ')] for i in range(n)]

def intersection_circle_with_line(a, b, x, y, r):
    dx = b - a
    dy = y - x
    a = a * a + x * x
    b = b * b + y * y
    c = (r * r) * (dx * dx + dy * dy)
    d = a - b + c
    if d < 0:
        return None
    if d == 0:
        return (-c/(2*dx)) + a/(2*dx)
    if d > 0:
        t1 = (-c + d ** 0.5)/(2*dx)
        t2 = (-c - d ** 0.5)/(2*dx)
        return [t1, t2]

def count_hits(angle):
    hits = 0
    for x, y, r in opponents:
        a = r * cos(angle) + x
        b = r * sin(angle) + y
        ts = intersection_circle_with_line(a, b, x, y, r)
        if ts is None:
            continue
        for t in ts:
            if t > 0:
                hits += 1
    return hits

def binary_search(l, r, f):
    while r - l > 1e-9:
        m = (r + l) / 2
        if f(m):
            r = m
        else:
            l = m
    return r

def optimal_angle():
    max_hits = 0
    max_hits_angle = 0
    for angle in [0, pi/2, pi, 3*pi/2]:
        hits = count_hits(angle)
        if hits > max_hits:
            max_hits = hits
            max_hits_angle = angle
    return binary_search(max_hits_angle, max_hits_angle + pi/2, lambda x: count_hits(x) == max_hits)

print(count_hits(optimal_angle()))
