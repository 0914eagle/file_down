
def min_cost_to_jump(n, jump_lengths, costs):
    jump_dict = dict(zip(jump_lengths, costs))
    max_jump = max(jump_lengths)
    
    dp = [float('inf')] * (max_jump + 1)
    dp[0] = 0
    
    for i in range(1, max_jump + 1):
        for jump_length, cost in jump_dict.items():
            if i >= jump_length:
                dp[i] = min(dp[i], dp[i - jump_length] + cost)
    
    min_cost = min(dp)
    
    if min_cost == float('inf'):
        return -1
    else:
        return min_cost

# Input
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Output
print(min_cost_to_jump(n, jump_lengths, costs))
