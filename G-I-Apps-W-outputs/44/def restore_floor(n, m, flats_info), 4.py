
def restore_floor(n, m, flats_info):
    possible_floors = set()
    
    for flat, floor in flats_info:
        possible_floors.add((n - 1) // flat + 1)
    
    if len(possible_floors) == 1:
        return possible_floors.pop()
    else:
        return -1

# Input
n, m = map(int, input().split())
flats_info = [list(map(int, input().split())) for _ in range(m)]

# Output
print(restore_floor(n, m, flats_info))
```
