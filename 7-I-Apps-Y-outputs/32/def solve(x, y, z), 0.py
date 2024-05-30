
import sys

def solve(x, y, z):
    return (x-2*z)//(y+z)

x, y, z = map(int, sys.stdin.readline().split())
print(solve(x, y, z))

