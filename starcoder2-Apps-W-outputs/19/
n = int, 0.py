
n = int(input())
x = []
y = []
for i in range(n):
    a, b = map(int, input().split())
    x.append(a)
    y.append(b)
x.sort()
y.sort()
print(max(x[n-1]-x[0], y[n-1]-y[0]))
