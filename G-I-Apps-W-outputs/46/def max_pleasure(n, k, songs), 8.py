
def max_pleasure(n, k, songs):
    songs_sorted = sorted(songs, key=lambda x: x[1], reverse=True)
    total_length = 0
    max_beauty = 0
    pleasure = 0

    for i in range(k):
        total_length += songs_sorted[i][0]
        max_beauty = max(max_beauty, songs_sorted[i][1])
        pleasure = max(pleasure, total_length * max_beauty)

    return pleasure

# Input
n, k = map(int, input().split())
songs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_pleasure(n, k, songs))
```
