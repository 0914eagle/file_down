
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_indices = {word: i for i, word in enumerate(words)}
    group_costs = {group_idx: min(costs[word_indices[word]] for word in group) for group_idx, group in groups.items()}

    total_cost = 0
    for word in message:
        word_idx = word_indices[word]
        cost = group_costs[word_idx] if word_idx in group_costs else costs[word_idx]
        total_cost += cost

    return total_cost

# Read input
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))

groups = {}
for _ in range(k):
    group_info = list(map(int, input().split()))
    group_idx = group_info[0]
    group_words = group_info[1:]
    groups.update({word_idx: group_words for word_idx in group_words})

message = input().split()

# Calculate and print the minimum cost
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
