
def solve():
    n, m = map(int, input().split())
    ships = [map(int, input().split()) for i in range(m)]
    ships = sorted(ships, key=lambda x: x[2], reverse=True)
    x = [1 for i in range(n+1)]
    y = [-1 for i in range(n+1)]
    flag = True
    for s in ships:
        x1, x2, y = s
        for i in range(x1, x2+1):
            if y == x[i] or y == y[i]:
                flag = False
                break
            x[i] = y[i] = y
    if not flag:
        print('impossible')
        return
    ans = ['' for i in range(n+1)]
    for i in range(1, n+1):
        if x[i] == y[i]:
            ans[i] = '0'
        else:
            ans[i] = '-' if x[i] < y[i] else '+'
    print(''.join(ans))


solve()
