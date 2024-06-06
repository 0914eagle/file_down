
for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())

    print(min(x*b, y*b, (x+y)*a))
