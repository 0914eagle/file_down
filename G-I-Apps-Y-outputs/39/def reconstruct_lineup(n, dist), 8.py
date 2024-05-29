
def reconstruct_lineup(n, dist):
    lineup = [1] * n
    for i in range(1, n):
        count = 0
        for j in range(i-1, -1, -1):
            if count == dist[j]:
                lineup[i] = lineup[j] + 1
                break
            if lineup[j] >= lineup[i]:
                lineup[j] += 1
            count += 1
    return lineup

# Input
n = int(input())
dist = list(map(int, input().split()))

# Reconstruct lineup
result = reconstruct_lineup(n, dist)

# Output
print(" ".join(map(str, result)))
```
