
x, y, x0, y0 = map(int, input().split())
s = input()

def get_next_pos(x, y, d):
    if d == 'L':
        y -= 1
    elif d == 'R':
        y += 1
    elif d == 'U':
        x -= 1
    elif d == 'D':
        x += 1
    return x, y

def get_next_pos_with_mine(x, y, d, xm, ym):
    if d == 'L':
        y -= 1
        if y == ym and x == xm:
            return -1, -1
    elif d == 'R':
        y += 1
        if y == ym and x == xm:
            return -1, -1
    elif d == 'U':
        x -= 1
        if y == ym and x == xm:
            return -1, -1
    elif d == 'D':
        x += 1
        if y == ym and x == xm:
            return -1, -1
    return x, y

ans = [0] * (len(s) + 1)

for i in range(1, x * y + 1):
    xm, ym = divmod(i - 1, y)
    xm += 1
    ym += 1
    if xm == x0 and ym == y0:
        continue
    x, y = x0, y0
    for j in range(len(s)):
        x, y = get_next_pos(x, y, s[j])
        if x == -1 and y == -1:
            break
    else:
        ans[len(s)] += 1
    for j in range(len(s)):
        x, y = get_next_pos_with_mine(x, y, s[j], xm, ym)
        if x == -1 and y == -1:
            break
    else:
        ans[j] += 1

print(*ans)
