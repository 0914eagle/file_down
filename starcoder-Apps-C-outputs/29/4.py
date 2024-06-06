
# coding: utf-8
# Your code here!
n = int(input())
a = [list(map(int, input().split())) for i in range(n)]

ans = 0.0
for i in range(n):
    x1, y1 = a[i]
    x2, y2 = a[(i + 1) % n]

    ans += (x1 + x2) * (y1 - y2)

print(abs(ans) / 2.0 / n)
