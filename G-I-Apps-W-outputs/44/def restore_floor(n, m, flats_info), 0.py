
def restore_floor(n, m, flats_info):
    possible_floors = set()
    
    for k, f in flats_info:
        possible_floors.add((k-1) // f + 1)
    
    if len(possible_floors) == 1:
        return list(possible_floors)[0]
    else:
        return -1

# Input processing
n, m = map(int, input().split())
flats_info = [list(map(int, input().split())) for _ in range(m)]

# Output
print(restore_floor(n, m, flats_info))
```
