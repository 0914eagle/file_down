
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_indices = {word: i for i, word in enumerate(words)}
    group_costs = {i: min(costs[idx] for idx in group) for i, group in groups.items()}
    
    total_cost = 0
    for word in message:
        idx = word_indices[word]
        total_cost += costs[idx]
        
    for group in groups.values():
        min_group_cost = min(group_costs[i] for i in group)
        total_cost -= min_group_cost
    
    return total_cost

# Input
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = {}
for _ in range(k):
    x, *group_indices = map(int, input().split())
    groups[_] = group_indices
message = input().split()

# Output
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
