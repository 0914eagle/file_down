
def restore_floor(n, flats_memory):
    possible_floors = set()
    
    for k, f in flats_memory:
        possible_floors.add((k - 1) // f + 1)
    
    if len(possible_floors) == 1:
        return list(possible_floors)[0]
    else:
        return -1

# Input parsing
n, m = map(int, input().split())
flats_memory = [list(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
print(restore_floor(n, flats_memory))
```
