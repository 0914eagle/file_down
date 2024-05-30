
def min_cost_language(n, k, m, words, costs, groups, message):
    word_cost = {word: cost for word, cost in zip(words, costs)}
    group_map = {i+1: set(indices) for i, (size, *indices) in enumerate(groups)}

    total_cost = 0
    for word in message:
        if word not in word_cost:
            continue
        cost = word_cost[word]
        group_indices = {group: word_cost[words[idx-1]] for group, indices in group_map.items() if word in indices}
        min_cost = min(group_indices.values()) if group_indices else cost
        total_cost += min_cost

    return total_cost

# Input
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = [list(map(int, input().split())) for _ in range(k)]
message = input().split()

# Output
print(min_cost_language(n, k, m, words, costs, groups, message))
```
