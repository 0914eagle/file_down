
h, n = map(int, input().split())
spells = [tuple(map(int, input().split())) for _ in range(n)]
min_mp = [float('inf')] * (h + 1)
min_mp[0] = 0
for health in range(1, h + 1):
    for a, b in spells:
        if health >= a and min_mp[health - a] + b < min_mp[health]:
            min_mp[health] = min_mp[health - a] + b
print(min_mp[h])

