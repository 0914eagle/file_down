
n = int(input())

x1 = []
x2 = []
y1 = []
y2 = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    x2.append(c)
    y1.append(b)
    y2.append(d)

x1.sort()
x2.sort()
y1.sort()
y2.sort()

if x1[0] == x1[n - 1] and x2[0] == x2[n - 1] and y1[0] == y1[n - 1] and y2[0] == y2[n - 1]:
    print("YES")
else:
    print("NO")
