
def count_ways_to_paint(N, M, blue_params):
    MOD = 100003
    
    total_ways = 1
    for i in range(N):
        total_ways *= (M - blue_params[i] - i)
        total_ways %= MOD
    
    return total_ways, total_ways % MOD

# Input
N, M = map(int, input().split())
blue_params = list(map(int, input().split()))

# Output
result = count_ways_to_paint(N, M, blue_params)
print(*result)
