
import sys

for i in range(int(input())):
    x, y = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())

    if x > y:
        x, y = y, x

    print(min(x,y) * a + abs(x - y) * b)
