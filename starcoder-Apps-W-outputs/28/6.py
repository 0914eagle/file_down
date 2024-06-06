
for _ in range(int(input())):
    x, y = map(int, input().split())
    a, b = map(int, input().split())
    ans = 0
    while x > 0 and y > 0:
        if x > y:
            x -= 1
            ans += a
        else:
            y -= 1
            ans += a
    while x != 0 or y != 0:
        x += 1
        y += 1
        ans += b
    print(ans)
