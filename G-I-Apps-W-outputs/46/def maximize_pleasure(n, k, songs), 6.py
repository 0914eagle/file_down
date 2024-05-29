
def maximize_pleasure(n, k, songs):
    songs.sort(key=lambda x: x[1], reverse=True)
    max_pleasure = 0
    length_sum = 0
    beauty_min = float('inf')
    
    for i in range(min(n, k)):
        length_sum += songs[i][0]
        beauty_min = min(beauty_min, songs[i][1])
        pleasure = length_sum * beauty_min
        max_pleasure = max(max_pleasure, pleasure)
    
    return max_pleasure

# Input
n, k = map(int, input().split())
songs = []
for _ in range(n):
    t, b = map(int, input().split())
    songs.append((t, b))

# Output
print(maximize_pleasure(n, k, songs))
```
