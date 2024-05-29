
def max_pleasure(n, k, playlist):
    playlist.sort(key=lambda x: x[1], reverse=True)
    max_pleasure = 0
    beauty = playlist[k-1][1]
    for i in range(k):
        max_pleasure += beauty * playlist[i][0]
    return max_pleasure

# Read input
n, k = map(int, input().split())
playlist = [list(map(int, input().split())) for _ in range(n)]

# Calculate and print output
print(max_pleasure(n, k, playlist))
```
