
def min_cost_to_jump(n, lengths, costs):
    max_jump = max(lengths)
    dp = [float('inf')] * (max_jump + 1)
    dp[0] = 0

    for i in range(1, max_jump + 1):
        for j in range(n):
            if i >= lengths[j]:
                dp[i] = min(dp[i], dp[i - lengths[j]] + costs[j])

    result = float('inf')
    for i in range(1, max_jump + 1):
        if dp[i] < float('inf'):
            result = min(result, dp[i])

    return result if result < float('inf') else -1

# Input parsing
n = int(input())
lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and output the result
print(min_cost_to_jump(n, lengths, costs))
