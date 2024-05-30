
import sys

n = int(input())

for i in range(1, n + 1):
    c, s, f = map(int, sys.stdin.readline().split())
    if i == 1:
        print(s + c)
    else:
        print((s - s % f) + c)

