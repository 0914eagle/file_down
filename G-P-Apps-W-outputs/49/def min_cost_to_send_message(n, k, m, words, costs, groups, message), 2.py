
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_to_cost = dict(zip(words, costs))
    group_to_words = {}
    for i in range(k):
        group_info = groups[i]
        group_to_words[i] = [words[idx-1] for idx in group_info[1:]]

    total_cost = 0
    for word in message:
        if word in word_to_cost:
            min_cost = word_to_cost[word]
            for group_words in group_to_words.values():
                if word in group_words:
                    for group_word in group_words:
                        if group_word in word_to_cost:
                            min_cost = min(min_cost, word_to_cost[group_word])
            total_cost += min_cost

    return total_cost

# Input parsing
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = [list(map(int, input().split())) for _ in range(k)]
message = input().split()

result = min_cost_to_send_message(n, k, m, words, costs, groups, message)
print(result)
```
