
n, m = map(int, input().split())
chests = list(map(int, input().split()))
keys = list(map(int, input().split()))
chests.sort()
keys.sort()
i, j, res = 0, 0, 0
while i < n and j < m:
    if (chests[i] + keys[j]) % 2 == 1:
        res += 1
        i += 1
        j += 1
    elif chests[i] < keys[j]:
        i += 1
    else:
        j += 1
print(res)

