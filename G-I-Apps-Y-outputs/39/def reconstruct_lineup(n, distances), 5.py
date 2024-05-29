
def reconstruct_lineup(n, distances):
    lineup = [1]
    for i in range(n - 1):
        lineup.insert(distances[i], i + 2)
    return lineup

n = int(input())
distances = list(map(int, input().split()))

result = reconstruct_lineup(n, distances)
print(*result)
```
