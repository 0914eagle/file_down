
def max_pleasure(n, k, songs):
    songs.sort(key=lambda x: x[1], reverse=True)
    total_length = 0
    min_beauty = float('inf')
    pleasure = 0

    for length, beauty in songs[:k]:
        total_length += length
        min_beauty = min(min_beauty, beauty)

    pleasure = total_length * min_beauty
    return pleasure

# Input parsing
n, k = map(int, input().split())
songs = []
for _ in range(n):
    t, b = map(int, input().split())
    songs.append((t, b))

# Calculate and output the maximum pleasure
print(max_pleasure(n, k, songs))
```
