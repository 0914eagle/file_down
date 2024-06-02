
n, b, a = map(int, input().split())
s = list(map(int, input().split()))

ans = 0

for i in range(n):
    if s[i] == 1 and b > 0:
        b -= 1
        a += 1
        ans += 1
    elif a > 0:
        a -= 1
        ans += 1

print(ans)

