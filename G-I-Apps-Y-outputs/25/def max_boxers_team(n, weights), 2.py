
def max_boxers_team(n, weights):
    weights_set = set(weights)
    count = 0
    for weight in weights:
        if weight in weights_set:
            count += 1
            weights_set.remove(weight)
        elif weight - 1 in weights_set:
            count += 1
            weights_set.remove(weight - 1)
        elif weight + 1 in weights_set:
            count += 1
            weights_set.remove(weight + 1)
    return count

n = int(input())
weights = list(map(int, input().split()))
print(max_boxers_team(n, weights))
```
