
def restore_floor(n, m, memories):
    possible_floors = set()
    
    for k, f in memories:
        possible_floors.add((k + f - 1) // k)
    
    if len(possible_floors) > 1:
        return -1
    
    return n // list(possible_floors)[0]

# Input
n, m = map(int, input().split())
memories = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(restore_floor(n, m, memories))
```
