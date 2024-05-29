
MOD = 998244353

def ways_to_make_figure_complete(N, parts):
    total_ways = 1
    total_holes = sum(parts)
    
    for d in parts:
        total_ways = (total_ways * (total_holes - d)) % MOD
        total_holes -= d
    
    for i in range(1, N):
        total_ways = (total_ways * i) % MOD
    
    return total_ways

# Read input
N = int(input())
parts = list(map(int, input().split()))

# Calculate and print the number of ways to make the figure complete
print(ways_to_make_figure_complete(N, parts))
```
