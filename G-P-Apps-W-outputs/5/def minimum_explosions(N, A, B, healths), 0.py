
def minimum_explosions(N, A, B, healths):
    explosions = 0
    for health in healths:
        if health <= A:
            explosions += 1
        else:
            remaining_health = health - A
            remaining_monsters = (remaining_health + (A - B) - 1) // (A - B)
            explosions += 1 + remaining_monsters
    return explosions

# Read input
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Calculate and print the minimum number of explosions needed
print(minimum_explosions(N, A, B, healths))
```
