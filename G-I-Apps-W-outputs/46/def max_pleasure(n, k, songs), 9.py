
def max_pleasure(n, k, songs):
    songs.sort(key=lambda x: x[1], reverse=True)
    max_pleasure = 0
    total_length = 0
    beauty_values = []

    for i in range(n):
        if i < k:
            total_length += songs[i][0]
            beauty_values.append(songs[i][1])
            max_pleasure = max(max_pleasure, total_length * min(beauty_values))
        else:
            if songs[i][1] > min(beauty_values):
                total_length += songs[i][0]
                beauty_values.append(songs[i][1])
                total_length -= songs[i - k][0]
                beauty_values.remove(songs[i - k][1])
                max_pleasure = max(max_pleasure, total_length * min(beauty_values))
    
    return max_pleasure

# Input
n, k = map(int, input().split())
songs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_pleasure(n, k, songs))
```
