
def solve(n, x, y):
    home = [0] * (10**5 + 1)
    away = [0] * (10**5 + 1)
    for i in range(n):
        home[x[i]] += 1
        away[y[i]] += 1
    
    for i in range(n):
        print(home[x[i]] - 1, away[y[i]] - 1)

n = int(input())
x = [0] * n
y = [0] * n
for i in range(n):
    x[i], y[i] = map(int, input().split())
solve(n, x, y)

