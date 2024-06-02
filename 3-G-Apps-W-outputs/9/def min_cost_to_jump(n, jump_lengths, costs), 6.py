
def min_cost_to_jump(n, jump_lengths, costs):
    max_jump = max(jump_lengths)
    reachable = set()
    
    for i in range(n):
        new_reachable = set()
        for cell in reachable:
            for j in range(-max_jump, max_jump+1):
                new_reachable.add(cell + j)
        reachable.update(new_reachable)
        reachable.add(0)
    
    if len(reachable) == 2*max_jump + 1:
        return -1
    
    min_cost = float('inf')
    for i in range(1, 2**n):
        total_cost = 0
        total_jump_lengths = 0
        for j in range(n):
            if i & (1 << j):
                total_cost += costs[j]
                total_jump_lengths += jump_lengths[j]
        if total_jump_lengths >= len(reachable):
            min_cost = min(min_cost, total_cost)
    
    return min_cost if min_cost != float('inf') else -1

# Input
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Output
print(min_cost_to_jump(n, jump_lengths, costs))
