
n, k = map(int, input().split())
w = list(map(int, input().split()))
ways = {0: 1}
for weight in w:
    new_ways = {}
    for total_weight in ways:
        if total_weight + weight <= k:
            new_ways[total_weight + weight] = ways[total_weight]
        if total_weight - weight >= 0:
            new_ways[total_weight - weight] = ways[total_weight]
    ways = new_ways
print(len(ways) if len(ways) > 0 else -1)
print(sum(ways.values()) % 1000000007)

