
def solve(n, x, y):
    x_count = [0] * (10**5 + 1)
    y_count = [0] * (10**5 + 1)
    
    for i in range(n):
        x_count[x[i]] += 1
        y_count[y[i]] += 1
        
    for i in range(n):
        print(x_count[x[i]] - 1, y_count[y[i]] - 1)

n = int(input())
x = [0] * n
y = [0] * n

for i in range(n):
    x[i], y[i] = map(int, input().split())
    
solve(n, x, y)
