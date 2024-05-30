
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_to_cost = {}
    for i in range(n):
        word_to_cost[words[i]] = costs[i]

    group_to_words = {}
    for i in range(k):
        group = groups[i]
        for j in range(1, len(group)):
            group_to_words[words[group[j] - 1]] = group[1]

    total_cost = 0
    for word in message:
        if word_to_cost[word] > word_to_cost[group_to_words[word]]:
            total_cost += word_to_cost[group_to_words[word]]
        else:
            total_cost += word_to_cost[word]

    return total_cost


# Input parsing
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = []
for _ in range(k):
    group_info = list(map(int, input().split()))
    groups.append(group_info)

message = input().split()

# Call the function and print the output
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
