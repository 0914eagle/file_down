
MOD = 998244353

def count_ways_to_complete_figure(N, holes):
    result = 1
    total_holes = sum(holes)
    
    for i in range(1, N + 1):
        result *= total_holes - (holes[i-1] - 1)
        result %= MOD
        total_holes -= holes[i-1]
        
    return result % MOD

# Input parsing
N = int(input())
holes = list(map(int, input().split()))

# Find the number of ways to make the figure complete
print(count_ways_to_complete_figure(N, holes))
```
