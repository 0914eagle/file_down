
n = int(input())
s = input()
m = []
for i in range(n):
    m.append(input())
cur = m[0].index('R')
now = 0
m[0][cur] = '.'
ans = 1
while now < n * n:
    if s[now % len(s)] == '>':
        if cur == n - 1 or m[now // n][cur + 1] == '#':
            now += 1
            continue
        cur += 1
        m[now // n][cur] = '.'
        now += 1
    elif s[now % len(s)] == '<':
        if cur == 0 or m[now // n][cur - 1] == '#':
            now += 1
            continue
        cur -= 1
        m[now // n][cur] = '.'
        now += 1
    elif s[now % len(s)] == '^':
        if now // n == 0 or m[now // n - 1][cur] == '#':
            now += 1
            continue
        m[now // n - 1][cur] = '.'
        now += 1
    else:
        if now // n == n - 1 or m[now // n + 1][cur] == '#':
            now += 1
            continue
        m[now // n + 1][cur] = '.'
        now += 1
if now > n * n:
    print(1)
else:
    print(n * n - now + 1)
