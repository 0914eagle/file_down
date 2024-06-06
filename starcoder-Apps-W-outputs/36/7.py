

from collections import Counter

def dist(p1, p2):
    return (p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2

def find_radius(n):
    print(n)
    if n < 2:
        return -1, -1

    p1 = input().split(' ')
    p2 = input().split(' ')

    return dist(p1, p2)

n = int(input())
m = int(input())

r1 = find_radius(n)
r2 = find_radius(m)

print(r1, r2)
