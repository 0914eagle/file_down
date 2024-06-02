
def count_ways_to_paint(N, M, blue_params):
    total_ways = 1
    mod = 100003

    for i in range(N):
        total_ways *= (M - blue_params[i] - i)
        total_ways %= mod

    return total_ways, total_ways % mod

# Input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Output
result_X, result_Y = count_ways_to_paint(N, M, blue_params)
print(result_X, result_Y)
