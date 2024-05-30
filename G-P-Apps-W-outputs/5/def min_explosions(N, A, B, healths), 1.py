
def min_explosions(N, A, B, healths):
    explosions = 0
    for i in range(N):
        health = healths[i]
        health -= B
        if health <= 0:
            explosions += 1
        else:
            remaining_explosions = (health + B - 1) // (A - B)
            explosions += max(1, remaining_explosions)
    return explosions

# Read input
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Calculate and print the minimum number of explosions
print(min_explosions(N, A, B, healths))
```
