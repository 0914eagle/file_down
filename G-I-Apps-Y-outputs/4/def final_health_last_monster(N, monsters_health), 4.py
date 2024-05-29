
def final_health_last_monster(N, monsters_health):
    min_health = min(monsters_health)
    return min_health

# Read input
N = int(input())
monsters_health = list(map(int, input().split()))

# Call the function and print the result
print(final_health_last_monster(N, monsters_health))
```
