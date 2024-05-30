
def min_explosions(N, A, B, healths):
    explosions = 0
    for health in healths:
        if health <= 0:
            continue
        health -= A
        explosions += 1
        if health <= 0:
            continue
        extra_explosions = health // (A - B)
        if health % (A - B) != 0:
            extra_explosions += 1
        explosions += extra_explosions
    return explosions

# Input processing
N, A, B = map(int, input().split())
healths = [int(input()) for _ in range(N)]

# Output
print(min_explosions(N, A, B, healths))
```
