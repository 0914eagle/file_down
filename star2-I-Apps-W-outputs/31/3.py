
def solve(n, x, y):
    x_count = {}
    y_count = {}
    for i in range(n):
        x_count[x[i]] = x_count.get(x[i], 0) + 1
        y_count[y[i]] = y_count.get(y[i], 0) + 1
    for i in range(n):
        print(x_count[x[i]] - 1, y_count[y[i]])

n = int(input())
x = []
y = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
solve(n, x, y)

