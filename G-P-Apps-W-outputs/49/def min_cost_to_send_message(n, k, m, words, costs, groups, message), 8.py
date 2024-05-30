
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_to_cost = {}  # Dictionary to store cost of sending each word
    for i in range(n):
        word_to_cost[words[i]] = costs[i]

    group_to_words = {}  # Dictionary to store words in each group
    for i in range(k):
        group_info = groups[i]
        num_words_in_group = group_info[0]
        words_in_group = group_info[1:]
        for word_idx in words_in_group:
            if num_words_in_group not in group_to_words:
                group_to_words[num_words_in_group] = []
            group_to_words[num_words_in_group].append(words[word_idx - 1])

    total_cost = 0
    for word in message:
        if word in word_to_cost:
            if len(group_to_words) > 0:
                min_cost_word = min(group_to_words[len(group_to_words.keys())], key=lambda x: word_to_cost[x])
                total_cost += word_to_cost[min_cost_word]
            else:
                total_cost += word_to_cost[word]

    return total_cost

# Read input
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))

groups = []
for _ in range(k):
    group_info = list(map(int, input().split()))
    groups.append(group_info)

message = input().split()

# Call the function and print the result
print(min_cost_to_send_message(n, k, m, words, costs, groups, message))
```
