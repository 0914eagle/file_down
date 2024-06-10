
t = int(input())
for _ in range(t):
    n = int(input())
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i], y[i] = map(int, input().split())
    x.sort()
    y.sort()
    path = ""
    for i in range(n):
        path += "R" * x[i]
        path += "U" * y[i]
    print("YES")
    print(path)

