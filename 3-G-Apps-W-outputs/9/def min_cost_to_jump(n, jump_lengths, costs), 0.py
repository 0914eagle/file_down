
def min_cost_to_jump(n, jump_lengths, costs):
    max_jump = max(jump_lengths)
    reachable = set()
    for i in range(n):
        new_reachable = set()
        for cell in reachable:
            new_reachable.add(cell - jump_lengths[i])
            new_reachable.add(cell + jump_lengths[i])
        reachable.update(new_reachable)
        reachable.add(jump_lengths[i])
    if all(i in reachable for i in range(-max_jump, max_jump+1)):
        return sum(costs)
    return -1

# Input parsing
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and print the result
print(min_cost_to_jump(n, jump_lengths, costs))
