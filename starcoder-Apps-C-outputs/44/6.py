
# coding:utf-8
# 1000ms 32mb
import sys
import os

'''
1 1 2 3 1 0
2 4 20
'''

def main():
    x0, y0, ax, ay, bx, by = map(int, sys.stdin.readline().strip().split())
    xs, ys, t = map(int, sys.stdin.readline().strip().split())
    c = 0
    i = 0
    while True:
        tx = x0 * ax + bx
        ty = y0 * ay + by
        if tx == xs and ty == ys:
            c += 1
            break
        if abs(tx - xs) + abs(ty - ys) > t:
            break
        t -= abs(tx - xs) + abs(ty - ys)
        x0, y0 = tx, ty
        i += 1
        c += 1
    print(c)


if __name__ == "__main__":
    main()
