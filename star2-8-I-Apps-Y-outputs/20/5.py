
n = int(input())
max_div = 0
ans = 0
for i in range(1, n+1):
    div = 0
    tmp = i
    while tmp % 2 == 0:
        div += 1
        tmp //= 2
    if div > max_div:
        max_div = div
        ans = i
print(ans)

