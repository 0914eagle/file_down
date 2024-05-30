
def calculate_song_restarts(T, S, q):
    restarts = 0
    while S < T:
        S *= q
        restarts += 1
    return restarts + 1

# Input
T, S, q = map(int, input().split())

# Output
print(calculate_song_restarts(T, S, q))
```
