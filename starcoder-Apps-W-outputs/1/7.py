
import sys
input = sys.stdin.readline
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = [0] * (n + 1)
    for _ in range(m):
        x, y = map(int, input().split())
        a[x] += 1
        a[y] += 1
    b = sorted(a)
    if a[1] != b[1] or a[1] != b[n - 1]:
        print("NO")
    else:
        print("YES")
