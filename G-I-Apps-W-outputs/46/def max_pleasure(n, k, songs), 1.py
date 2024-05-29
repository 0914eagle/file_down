
def max_pleasure(n, k, songs):
    sorted_songs = sorted(songs, key=lambda x: x[1], reverse=True)
    
    max_pleasure = 0
    total_length = 0
    min_beauty = float('inf')
    
    for i in range(min(n, k)):
        total_length += sorted_songs[i][0]
        min_beauty = min(min_beauty, sorted_songs[i][1])
        max_pleasure = max(max_pleasure, total_length * min_beauty)
    
    return max_pleasure

# Input parsing
n, k = map(int, input().split())
songs = [tuple(map(int, input().split())) for _ in range(n)]

print(max_pleasure(n, k, songs))
```
