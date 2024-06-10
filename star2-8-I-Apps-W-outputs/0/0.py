
n, m = map(int, input().split())
chests = list(map(int, input().split()))
keys = list(map(int, input().split()))
chests.sort(reverse=True)
keys.sort(reverse=True)
ans = 0
i = 0
for chest in chests:
    while i < m and (keys[i] + chest) % 2 == 0:
        i += 1
    if i == m:
        break
    ans += 1
    i += 1
print(ans)

