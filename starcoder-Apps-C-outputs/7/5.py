
import math
n = int(input())
x = []
y = []
r = []

for i in range(n):
    a = input().split()
    x.append(int(a[0]))
    y.append(int(a[1]))
    r.append(int(a[2]))

max1 = 0
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        else:
            m = (y[i]-y[j])/(x[i]-x[j])
            angle = math.atan(m)
            xc = x[i]-x[j]
            yc = y[i]-y[j]
            radius = math.sqrt(xc**2+yc**2)
            angl = math.asin((r[j]+r[i])/radius)
            if 2*angl <= angle:
                max1 += 1
            elif 2*angl <= angle+math.pi:
                max1 += 2
            else:
                continue

print(max1)
