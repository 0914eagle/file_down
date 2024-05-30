
def restart_song(T, S, q):
    restarts = 0
    while S < T:
        S *= q
        restarts += 1
    return restarts + 1

# Read input
T, S, q = map(int, input().split())

# Call the function and print the output
print(restart_song(T, S, q))
```
