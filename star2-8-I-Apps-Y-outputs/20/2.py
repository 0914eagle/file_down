
n = int(input())

max_count = 0
ans = 1
for i in range(1, n + 1):
    count = 0
    while i % 2 == 0:
        i //= 2
        count += 1
    if max_count < count:
        max_count = count
        ans = i * 2

print(ans)

