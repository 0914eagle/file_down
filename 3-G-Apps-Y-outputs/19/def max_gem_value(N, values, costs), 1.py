
def max_gem_value(N, values, costs):
    max_value = 0
    for i in range(N):
        diff = values[i] - costs[i]
        if diff > 0:
            max_value += diff
    return max_value

# Input
N = int(input())
values = list(map(int, input().split()))
costs = list(map(int, input().split()))

# Output
print(max_gem_value(N, values, costs))
