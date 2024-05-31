
a, d = map(float, input().split())
n = int(input())

x = 0
y = 0
angle = 0

for i in range(1, n+1):
    x += d * (1 if angle == 0 else (-1 if angle == 90 else (1 if angle == 180 else -1)))
    y += d * (1 if angle == 90 else (-1 if angle == 180 else (1 if angle == 270 else -1)))
    print("{:.10f} {:.10f}".format(x, y))

    angle = (angle + 90) % 360
