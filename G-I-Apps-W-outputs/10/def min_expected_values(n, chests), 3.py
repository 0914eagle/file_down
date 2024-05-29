
# Function to calculate the minimum expected value of player's earnings
def min_expected_values(n, chests):
    MOD = 998244353
    
    # Sort the chests in descending order of treasure values
    chests.sort(reverse=True)
    
    # Prefix sum of treasure values to easily calculate sum of values in a range
    prefix_sum = [0] + [sum(chests[:i]) for i in range(1, n+1)]
    
    # Initialize minimum expected values with 0
    min_expected = [0] * n
    
    # Calculate the minimum expected values
    for k in range(1, n+1):
        for i in range(k, n+1):
            expected_val = prefix_sum[i] - prefix_sum[i-k]
            min_expected[k-1] = (min_expected[k-1] + expected_val) % MOD
        
    return min_expected

# Input
n = int(input())
chests = list(map(int, input().split()))

# Calculate and output the minimum expected values
result = min_expected_values(n, chests)
print(*result)
```
