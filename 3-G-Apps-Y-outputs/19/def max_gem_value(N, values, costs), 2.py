
def max_gem_value(N, values, costs):
    max_value = 0
    for i in range(2**N):
        selected_gems = []
        for j in range(N):
            if (i >> j) & 1:
                selected_gems.append(j)
        total_value = sum([values[k] for k in selected_gems])
        total_cost = sum([costs[k] for k in selected_gems])
        max_value = max(max_value, total_value - total_cost)
    return max_value

# Input
N = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Output
print(max_gem_value(N, values, costs))
