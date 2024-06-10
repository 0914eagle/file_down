
def solve(n, x, y):
    x_count = [0] * (10**5 + 1)
    y_count = [0] * (10**5 + 1)
    
    for i in range(n):
        x_count[x[i]] += 1
        y_count[y[i]] += 1
    
    for i in range(n):
        print(x_count[x[i]] - 1, y_count[y[i]] - 1)

n = int(input())
x = []
y = []
for i in range(n):
    x_i, y_i = map(int, input().split())
    x.append(x_i)
    y.append(y_i)
    
solve(n, x, y)

