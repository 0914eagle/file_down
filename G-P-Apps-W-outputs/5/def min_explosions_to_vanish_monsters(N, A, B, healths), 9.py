
def min_explosions_to_vanish_monsters(N, A, B, healths):
    min_explosions = 0
    for health in healths:
        if health <= A:
            min_explosions += 1
        else:
            remaining_health = health - A
            num_explosions = (remaining_health + (A - B) - 1) // (A - B)
            min_explosions += num_explosions + 1

    return min_explosions

# Read input
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Calculate and print the minimum number of explosions needed
print(min_explosions_to_vanish_monsters(N, A, B, healths))
```
