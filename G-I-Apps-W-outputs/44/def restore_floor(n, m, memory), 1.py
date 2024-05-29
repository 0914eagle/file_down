
def restore_floor(n, m, memory):
    possible_floors = set()
    for k, f in memory:
        possible_floors.add((k-1) // f + 1)
    
    if len(possible_floors) == 1:
        return (n-1) // list(possible_floors)[0] + 1
    else:
        return -1

n, m = map(int, input().split())
memory = [list(map(int, input().split())) for _ in range(m)]
print(restore_floor(n, m, memory))
