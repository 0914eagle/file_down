
for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    if x == y == 0:
        print(0)
    else:
        print(min(a, b) * 2 + abs(x - y) * max(a, b))
