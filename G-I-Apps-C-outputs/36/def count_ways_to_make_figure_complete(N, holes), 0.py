
def count_ways_to_make_figure_complete(N, holes):
    MOD = 998244353
    total_ways = 1
    for d in holes:
        total_ways = (total_ways * (d - 1)) % MOD
    result = 1
    for i in range(N - 2):
        result = (result * 2) % MOD
    return (result * total_ways) % MOD

# Read input from Standard Input
N = int(input())
holes = list(map(int, input().split()))

# Calculate and print the result
print(count_ways_to_make_figure_complete(N, holes))
```
