
def maximize_pleasure(n, k, songs):
    songs.sort(key=lambda x: -x[1])  # Sort songs by beauty in descending order
    total_length = 0
    max_beauty = 0
    pleasure = 0
    for i in range(k):
        total_length += songs[i][0]
        max_beauty = max(max_beauty, songs[i][1])
        pleasure = max(pleasure, total_length * max_beauty)
    return pleasure

# Reading input
n, k = map(int, input().split())
songs = [list(map(int, input().split())) for _ in range(n)]

# Call function and print output
print(maximize_pleasure(n, k, songs))
```
