
def min_cost_to_jump(n, jump_lengths, costs):
    max_jump = max(jump_lengths)
    reachable = [False] * (max_jump + 1)
    reachable[0] = True

    for i in range(n):
        new_reachable = [False] * (max_jump + 1)
        for j in range(max_jump + 1):
            if reachable[j]:
                new_reachable[jump_lengths[i]] = True
                if j - jump_lengths[i] >= 0:
                    new_reachable[j - jump_lengths[i]] = True
                if j + jump_lengths[i] <= max_jump:
                    new_reachable[j + jump_lengths[i]] = True
        reachable = new_reachable

    if all(reachable):
        return sum(costs)
    else:
        return -1

# Input parsing
n = int(input())
jump_lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and print the result
print(min_cost_to_jump(n, jump_lengths, costs))
