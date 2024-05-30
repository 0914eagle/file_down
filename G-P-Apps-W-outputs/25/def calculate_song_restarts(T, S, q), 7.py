
def calculate_song_restarts(T, S, q):
    times_restarted = 0
    while S < T:
        T //= q
        times_restarted += 1
    return times_restarted + 1

# Reading input values
T, S, q = map(int, input().split())

# Calling the function and printing the output
print(calculate_song_restarts(T, S, q))
```
