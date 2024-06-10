
n, m, k = map(int, input().split())
buildings = [0] * m
noise = 0
res = 0
for i in range(n):
    building = int(input())
    buildings[building - 1] += 1
    noise += buildings[building - 1]
    if i >= k:
        buildings[int(input()) - 1] -= 1
        noise -= buildings[int(input()) - 1]
    res = max(res, noise)
print(res)

