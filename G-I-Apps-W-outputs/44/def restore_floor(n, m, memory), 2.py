
def restore_floor(n, m, memory):
    possible_floors = set()
    for i in range(1, 101):  # Try all possible number of flats on each floor from 1 to 100
        valid = True
        for k, f in memory:
            floor = (k - 1) // i + 1
            if floor != f:
                valid = False
                break
        if valid:
            possible_floors.add((n - 1) // i + 1)
    if len(possible_floors) == 1:
        return possible_floors.pop()
    else:
        return -1

n, m = map(int, input().split())
memory = [tuple(map(int, input().split())) for _ in range(m)]
print(restore_floor(n, m, memory))
```
