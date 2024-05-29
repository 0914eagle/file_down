
def restore_floor(n, m, flats_info):
    possible_floors = set()
    
    for k, f in flats_info:
        possible_floors.add((k - 1) // f)
    
    if len(possible_floors) == 1:
        unique_floor = next(iter(possible_floors))
        return unique_floor + ((n - 1) // (unique_floor + 1))
    else:
        return -1

# Input parsing
n, m = map(int, input().split())
flats_info = [tuple(map(int, input().split())) for _ in range(m)]

# Call the function and print the output
print(restore_floor(n, m, flats_info))
```
