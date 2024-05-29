
def restore_floor(n, m, memory):
    possible_floors = set()
    
    for k, f in memory:
        possible_floors.add((k + f - 1) // f)
    
    if len(possible_floors) > 1:
        return -1
    else:
        return (n + list(possible_floors)[0] - 1) // list(possible_floors)[0]

# Input
n, m = map(int, input().split())
memory = [list(map(int, input().split())) for _ in range(m)]

# Output
print(restore_floor(n, m, memory))
```
