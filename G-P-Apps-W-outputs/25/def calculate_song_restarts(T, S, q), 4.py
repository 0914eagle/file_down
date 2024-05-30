
def calculate_song_restarts(T, S, q):
    restarts = 0
    while S < T:
        S *= q
        restarts += 1
    return restarts + 1

# Reading input values
T, S, q = map(int, input().split())

# Calculating and printing the number of times the song will be restarted
print(calculate_song_restarts(T, S, q))
```
