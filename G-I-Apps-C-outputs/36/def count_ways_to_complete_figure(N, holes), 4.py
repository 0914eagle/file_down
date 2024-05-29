
MOD = 998244353

def count_ways_to_complete_figure(N, holes):
    total_ways = 1
    for d in holes:
        total_ways *= d
        total_ways %= MOD
    
    return total_ways

N = int(input())
holes = list(map(int, input().split()))

print(count_ways_to_complete_figure(N, holes))
```
