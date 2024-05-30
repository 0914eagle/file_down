
def song_restart(T, S, q):
    times_restarted = 0
    downloaded = S
    while downloaded < T:
        downloaded *= q
        times_restarted += 1
    return times_restarted + 1

# Input
T, S, q = map(int, input().split())

# Output
print(song_restart(T, S, q))
```
