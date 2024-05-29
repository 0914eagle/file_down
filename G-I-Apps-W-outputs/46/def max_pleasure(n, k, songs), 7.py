
def max_pleasure(n, k, songs):
    sorted_songs = sorted(songs, key=lambda x: x[1], reverse=True)
    max_pleasure = 0
    beauty_values = []
    
    for t, b in sorted_songs[:k]:
        beauty_values.append(b)
    
    min_beauty = min(beauty_values)
    
    for t, b in songs:
        max_pleasure = max(max_pleasure, t * min_beauty)
    
    return max_pleasure

# Input
n, k = map(int, input().split())
songs = [list(map(int, input().split())) for _ in range(n)]

# Output
print(max_pleasure(n, k, songs))
