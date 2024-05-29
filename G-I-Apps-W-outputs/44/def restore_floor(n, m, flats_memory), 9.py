
def restore_floor(n, m, flats_memory):
    possible_floors = set()
    
    for flat, floor in flats_memory:
        possible_floors.add((n - flat + floor) // 2)
    
    if len(possible_floors) == 1:
        return possible_floors.pop()
    else:
        return -1

# Input
n, m = map(int, input().split())
flats_memory = [tuple(map(int, input().split())) for _ in range(m)]

# Output
print(restore_floor(n, m, flats_memory))
```
