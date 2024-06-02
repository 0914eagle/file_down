
n = int(input())

ans = 1
for i in range(1, n+1):
    cnt = 0
    while i % 2 == 0:
        i //= 2
        cnt += 1
    if cnt > ans:
        ans = cnt

print(ans)

