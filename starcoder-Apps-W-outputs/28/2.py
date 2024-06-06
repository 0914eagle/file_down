
import sys
def solve(x, y, a, b):
    ans = 0
    if x > y:
        ans += a * (x - y)
        x = y
    elif y > x:
        ans += b * (y - x)
        y = x
    return ans

for _ in range(int(sys.stdin.readline().strip())):
    x, y = list(map(int, sys.stdin.readline().strip().split()))
    a, b = list(map(int, sys.stdin.readline().strip().split()))
    print(solve(x, y, a, b))
