
from itertools import combinations

n, k = map(int, input().split())
weights = list(map(int, input().split()))

ways = [[[i] for i in range(n) if weights[i] <= k]]
for i in range(1, n):
    ways.append([])
    for way in ways[i - 1]:
        if weights[way[-1]] + weights[i] <= k:
            ways[i].append(way + [i])

if not ways[n - 1]:
    print(-1)
    print(0)
else:
    min_rides = len(ways[n - 1][0])
    num_ways = 0
    for way in ways[n - 1]:
        if len(way) == min_rides:
            num_ways += 1
    print(min_rides)
    print(num_ways % 1000000007)

