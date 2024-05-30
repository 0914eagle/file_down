
def min_explosions_to_vanish_monsters(N, A, B, healths):
    def calculate_explosions_needed(health):
        if health <= 0:
            return 0
        return (health + B - 1) // B

    total_explosions = 0
    for health in healths:
        total_explosions += calculate_explosions_needed(health)

    return total_explosions

# Read input
input_values = list(map(int, input().split()))
N, A, B = input_values[0], input_values[1], input_values[2]
healths = [int(input()) for _ in range(N)]

# Calculate and print the minimum number of explosions required
print(min_explosions_to_vanish_monsters(N, A, B, healths))
```
