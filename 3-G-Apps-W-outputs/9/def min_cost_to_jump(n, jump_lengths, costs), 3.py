
def min_cost_to_jump(n, jump_lengths, costs):
    max_jump = max(jump_lengths)
    
    reachable = set()
    for i in range(n):
        reachable.add(jump_lengths[i])
    
    for i in range(n):
        new_reachable = set()
        for j in range(1, max_jump+1):
            if j in reachable:
                new_reachable.add(j)
            elif j - jump_lengths[i] in reachable:
                new_reachable.add(j)
        reachable = reachable.union(new_reachable)
    
    if len(reachable) == max_jump:
        return sum(costs)
    else:
        return -1

# Input parsing
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and print the result
print(min_cost_to_jump(n, jump_lengths, costs))
