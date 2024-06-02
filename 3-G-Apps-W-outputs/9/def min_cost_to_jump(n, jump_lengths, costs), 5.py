
def min_cost_to_jump(n, jump_lengths, costs):
    jump_dict = {}
    for i in range(n):
        jump_dict[jump_lengths[i]] = min(jump_dict.get(jump_lengths[i], float('inf')), costs[i])
    
    sorted_jumps = sorted(jump_dict.items())
    
    dp = {0: 0}
    for i in range(1, sorted_jumps[-1][0] + 1):
        dp[i] = min(dp.get(i - jump, float('inf')) + cost for jump, cost in sorted_jumps)
    
    if dp[0] == 0:
        return 0
    
    min_cost = min(dp.values())
    return min_cost if min_cost < float('inf') else -1

# Input parsing
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and print the result
print(min_cost_to_jump(n, jump_lengths, costs))
