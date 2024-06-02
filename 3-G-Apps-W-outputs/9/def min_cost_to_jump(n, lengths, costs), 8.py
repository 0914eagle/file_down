
def min_cost_to_jump(n, lengths, costs):
    max_jump = max(lengths)
    reachable = [False] * (max_jump + 1)
    reachable[0] = True

    for i in range(n):
        for j in range(max_jump + 1):
            if reachable[j]:
                if j + lengths[i] <= max_jump:
                    reachable[j + lengths[i]] = True

    min_cost = float('inf')
    for i in range(1, max_jump + 1):
        if reachable[i]:
            min_cost = min(min_cost, costs[i-1])

    return min_cost if min_cost != float('inf') else -1

# Input parsing
n = int(input())
lengths = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Call the function and print the result
print(min_cost_to_jump(n, lengths, costs))
