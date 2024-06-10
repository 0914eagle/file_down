
def count_ways(total_weight, boat_weight_limit, weights, people):
    rides = 0
    ways = 1
    return rides, ways

n, k = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]
rides, ways = count_ways(sum(weights), k, weights, n)
if rides == -1:
    print(rides)
else:
    print(rides)
    print(ways % 1000000007)

