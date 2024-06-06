
x, y, x0, y0 = map(int, input().split())
s = input()

def check(x, y, x0, y0):
    if x < 1 or x > x or y < 1 or y > y:
        return False
    if x == x0 and y == y0:
        return False
    return True

def move(x, y, x0, y0, s):
    if s == 'L':
        y -= 1
    elif s == 'R':
        y += 1
    elif s == 'U':
        x -= 1
    elif s == 'D':
        x += 1
    return x, y

def solve(x, y, x0, y0, s):
    ans = [0] * (len(s) + 1)
    ans[0] = 1
    for i in range(len(s)):
        x, y = move(x, y, x0, y0, s[i])
        if check(x, y, x0, y0):
            ans[i + 1] = ans[i]
        else:
            ans[i + 1] = ans[i] - 1
    return ans

print(*solve(x, y, x0, y0, s))
