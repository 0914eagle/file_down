
def is_perfect_square(num):
    sqrt = int(num ** 0.5)
    return sqrt * sqrt == num

def shortest_subsequence_length(n, arr):
    dp = [set() for _ in range(n)]
    
    for i in range(n):
        dp[i].add(arr[i])
        for j in range(i):
            product = arr[i] * arr[j]
            if is_perfect_square(product):
                dp[i].add(arr[j])
                dp[i].add(arr[i])
                dp[i].update(dp[j])
    
    min_length = float('inf')
    for subset in dp:
        if len(subset) > 1:
            min_length = min(min_length, len(subset))
    
    return min_length if min_length != float('inf') else -1

# Input reading
n = int(input())
arr = list(map(int, input().split()))

# Output
print(shortest_subsequence_length(n, arr))
