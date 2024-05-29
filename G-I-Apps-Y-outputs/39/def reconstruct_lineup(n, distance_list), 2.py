
def reconstruct_lineup(n, distance_list):
    lineup = [1]  # Jimmy is always first
    for distance in distance_list:
        lineup.insert(distance, len(lineup) + 1)  # Insert the person at the specific distance from Jimmy
    return lineup

# Input reading
n = int(input())
distance_list = list(map(int, input().split()))

# Reconstruct the lineup and print the result
lineup = reconstruct_lineup(n, distance_list)
print(' '.join(map(str, lineup)))
```
