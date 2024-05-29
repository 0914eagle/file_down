
def restore_floor(n, m, flats_info):
    floors = set()
    for flat, floor in flats_info:
        floors.add((flat - 1) // floor)

    possible_floors = set(range(1, 101))
    for floor in floors:
        for i in range(1, 101):
            if ((i - 1) // floor) not in floors:
                possible_floors.discard(i)

    if len(possible_floors) == 1:
        return possible_floors.pop()
    else:
        return -1

n, m = map(int, input().split())
flats_info = [tuple(map(int, input().split())) for _ in range(m)]

result = restore_floor(n, m, flats_info)
print(result)
```
