

s, b = map(int, input().split())

spaceships = list(map(int, input().split()))

defe = [list(map(int, input().split())) for _ in range(b)]

defe.sort(key=lambda x: x[0])

ans = [0 for i in range(s)]

i = 0

for x in spaceships:
    while defe[i][0] <= x and i < b:
        ans[spaceships.index(x)] += defe[i][1]
        i += 1

for i in ans:
    print(i, end=" ")
