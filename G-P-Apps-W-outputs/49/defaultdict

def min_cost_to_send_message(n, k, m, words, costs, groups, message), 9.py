
from collections import defaultdict

def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_indices = {word: i for i, word in enumerate(words)}
    group_costs = defaultdict(list)
    
    for group in groups:
        x, *indices = group
        min_cost = float('inf')
        for idx in indices:
            min_cost = min(min_cost, costs[idx - 1])
        for idx in indices:
            group_costs[idx - 1].append(min_cost)
    
    total_cost = 0
    message_indices = [word_indices[word] for word in message]
    for idx in message_indices:
        total_cost += min(group_costs[idx]) if idx in group_costs else costs[idx]
    
    return total_cost

# Input parsing
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))

groups = []
for _ in range(k):
    group = list(map(int, input().split()))
    groups.append(group)

message = input().split()

# Output
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
