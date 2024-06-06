
from math import *
from fractions import Fraction
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
def side_len(pt):
    return (pt[0]-points[0][0])**2 + (pt[1]-points[0][1])**2
def dist(pt1, pt2):
    return sqrt(side_len(pt1) + side_len(pt2) - 2*pt1[0]*pt2[0] - 2*pt1[1]*pt2[1])
def area(pt1, pt2, pt3):
    return abs(pt1[0]*pt2[1] + pt2[0]*pt3[1] + pt3[0]*pt1[1] - pt1[0]*pt3[1] - pt3[0]*pt2[1] - pt2[0]*pt1[1])
def signed_area(pt1, pt2, pt3):
    return pt1[0]*pt2[1] + pt2[0]*pt3[1] + pt3[0]*pt1[1] - pt1[0]*pt3[1] - pt3[0]*pt2[1] - pt2[0]*pt1[1]
def height(pt1, pt2, pt3):
    return area(pt1, pt2, pt3) / dist(pt1, pt2)
s = 0
for i in range(n-1):
    h = height(points[i], points[i+1], points[i+2])
    if abs(signed_area(points[i], points[i+1], points[i+2])) < 10**(-6):
        s += h / 2
    else:
        s += h
print(s / n)
