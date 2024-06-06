
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# author:  <>
# 2017/10/07

import sys
import math

class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)
    def __repr__(self):
        return self.__str__()
    def distance(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

if __name__ == "__main__":
    n, m = map(int, sys.stdin.readline().strip().split(' '))
    points_m = []
    points_s = []
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        points_m.append(Point(x, y))
    for i in range(m):
        x, y = map(int, sys.stdin.readline().strip().split(' '))
        points_s.append(Point(x, y))
    max_distance = 0
    for p_m in points_m:
        for p_s in points_s:
            max_distance = max(max_distance, p_m.distance(p_s))
    r = max_distance / 2
    is_circle_possible = True
    for p_m in points_m:
        if p_m.distance(Point(0, 0)) > r:
            is_circle_possible = False
            break
    for p_s in points_s:
        if p_s.distance(Point(0, 0)) < r:
            is_circle_possible = False
            break
    if is_circle_possible:
        print("YES")
    else:
        print("NO")
