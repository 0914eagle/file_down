
def reconstruct_lineup(n, distances):
    lineup = [1]
    for d in distances:
        lineup.insert(d, len(lineup) + 1)
    return lineup

n = int(input())
distances = list(map(int, input().split()))

result = reconstruct_lineup(n, distances)
print(*result)
```
