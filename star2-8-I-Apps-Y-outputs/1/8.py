
n, k = map(int, input().split())
a = list(map(int, input().split()))
if len(set(a)) < k:
    print('NO')
else:
    print('YES')
    color = 1
    ans = []
    for i in range(n):
        if color > k:
            color = 1
        ans.append(color)
        color += 1
    print(*ans)

