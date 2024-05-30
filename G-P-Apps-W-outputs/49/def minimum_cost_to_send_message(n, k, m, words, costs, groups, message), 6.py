
def minimum_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_to_cost = {word: cost for word, cost in zip(words, costs)}
    group_to_words = {}
    for i in range(k):
        line = groups[i].split()
        x = int(line[0])
        group_words = [words[int(line[j + 1]) - 1] for j in range(x)]
        for word in group_words:
            group_to_words[word] = min(word_to_cost[word] for word in group_words)
    
    total_cost = 0
    for word in message:
        total_cost += word_to_cost[word] if word_to_cost[word] < group_to_words[word] else group_to_words[word]
    
    return total_cost

# Input
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))
groups = [input() for _ in range(k)]
message = input().split()

# Output
print(minimum_cost_to_send_message(n, k, m, words, costs, groups, message))
```
