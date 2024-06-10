
for _ in range(int(input())):
    a, b, n, m = map(int, input().split())
    for i in range(n+m):
        if a > b:
            a -= 1
        else:
            b -= 1
    print("Yes" if a >= 0 and b >= 0 else "No")

