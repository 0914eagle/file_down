
import sys

def solve(n):
    if n & 1:
        return (n+1)//2 * n - (n+1)//2 * (n//2)
    else:
        return n//2 * (n+1) - n//2 * (n//2)

for _ in range(int(input())):
    n = int(sys.stdin.readline().strip())
    print(solve(n))

