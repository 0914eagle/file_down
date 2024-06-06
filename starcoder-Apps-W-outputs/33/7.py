
import bisect

n = int(input())

a = []
for _ in range(n):
    m, *d = map(int, input().split())
    for x in d:
        bisect.insort(a, x)

if len(a) == n:
    print("impossible")
else:
    x = a.pop(0)
    for i in range(1, n):
        print(i, 1, x)
        x = a.pop(0)
