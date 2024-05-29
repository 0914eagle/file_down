
MOD = 998244353

def count_ways_to_make_figure_complete(N, di):
    total_ways = 1

    for i in range(N):
        total_ways = (total_ways * di[i]) % MOD

    return total_ways

# Read input
N = int(input())
di = list(map(int, input().split()))

# Calculate and print the answer
result = count_ways_to_make_figure_complete(N, di)
print(result)
```
