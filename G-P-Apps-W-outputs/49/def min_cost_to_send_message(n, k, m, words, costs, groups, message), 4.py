
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_indices = {word: i for i, word in enumerate(words)}
    group_costs = {}
    for group in groups:
        group_cost = min(costs[word_indices[word]] for word in group[1:])
        for word in group[1:]:
            group_costs[word_indices[word]] = group_cost

    total_cost = sum(costs[word_indices[word]] for word in message)
    for word in message:
        total_cost -= costs[word_indices[word]]
        total_cost += group_costs[word_indices[word]]
    
    return total_cost

# Input parsing
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = [list(map(int, input().split())) for _ in range(k)]
message = input().split()

# Calculate and print the minimum cost
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
