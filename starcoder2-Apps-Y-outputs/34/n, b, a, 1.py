
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

ans = 0
for i in range(n):
    if s[i] == 1:
        if b > 0:
            b -= 1
            ans += 1
        elif a > 0:
            a -= 1
            ans += 1
    else:
        if a > 0:
            a -= 1
            ans += 1
        elif b > 0:
            b -= 1
            ans += 1
print(ans)

