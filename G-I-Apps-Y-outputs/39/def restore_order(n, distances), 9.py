
def restore_order(n, distances):
    lineup = [1]
    for i in range(1, n):
        lineup.insert(distances[i-1], i+1)
    return lineup

# Read input
n = int(input())
distances = list(map(int, input().split()))

# Restore order and print result
lineup = restore_order(n, distances)
print(*lineup)
```
