
# Python3
n = int(input())

x, y = [0], [0]
for i in range(n):
	x_i, y_i = map(int, input().split())
	x.append(x_i)
	y.append(y_i)

x.append(x[1])
y.append(y[1])

area = 0
for i in range(1, n + 1):
	area += x[i] * y[i + 1] - y[i] * x[i + 1]
area = abs(area)

ans = 0
for i in range(1, n + 1):
	ans += (x[i] + x[i + 1]) * (y[i] - y[i + 1])
ans = abs(ans)

print(ans / (6 * area))
