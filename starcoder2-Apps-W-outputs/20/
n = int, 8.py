
n = int(input())

x = []
y = []

for i in range(n):
    a, b, c, d = map(int, input().split())
    x.append(a)
    x.append(c)
    y.append(b)
    y.append(d)

x.sort()
y.sort()

if x[0] == x[n] and x[1] == x[n+1] and y[0] == y[n] and y[1] == y[n+1]:
    print("YES")
else:
    print("NO")
