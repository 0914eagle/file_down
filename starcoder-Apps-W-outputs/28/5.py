
import sys

for i in range(int(sys.stdin.readline())):
    x, y = map(int, sys.stdin.readline().split())
    a, b = map(int, sys.stdin.readline().split())
    print(min(a,b) * abs(x-y))
