ath

def count_complete_figures(N, D):
    total_ways = 1
    for d in D:
        total_ways = (total_ways * (d + 1)) % 998244353
    return total_ways

# Read input
N = int(input())
D = list(map(int, input().split()))

# Calculate and print the answer
print(count_complete_figures(N, D))
