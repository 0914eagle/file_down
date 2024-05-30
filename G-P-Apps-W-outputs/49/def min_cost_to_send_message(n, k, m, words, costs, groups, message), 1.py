
def min_cost_to_send_message(n, k, m, words, costs, groups, message):
    word_to_cost = {words[i]: costs[i] for i in range(n)}
    group_to_words = {}
    for i in range(k):
        group = groups[i]
        group_to_words[group[0]] = [words[idx-1] for idx in group[1:]]
    
    total_cost = 0
    for word in message:
        if word in group_to_words:
            min_cost = float('inf')
            for w in group_to_words[word]:
                min_cost = min(min_cost, word_to_cost[w])
            total_cost += min_cost
        else:
            total_cost += word_to_cost[word]
    
    return total_cost

# Input processing
n, k, m = map(int, input().split())
words = input().split()
costs = list(map(int, input().split()))

groups = []
for _ in range(k):
    group = list(map(int, input().split()))
    groups.append(group)

message = input().split()

# Call the function with input values
result = min_cost_to_send_message(n, k, m, words, costs, groups, message)
print(result)
```
