
def solve(n, x, y):
    x_dict = {}
    y_dict = {}
    for i in range(n):
        x_dict[x[i]] = x_dict.get(x[i], 0) + 1
        y_dict[y[i]] = y_dict.get(y[i], 0) + 1
    
    for i in range(n):
        print(x_dict[x[i]] + y_dict[x[i]] - 1, y_dict[y[i]])

n = int(input())
x = []
y = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
    
solve(n, x, y)

