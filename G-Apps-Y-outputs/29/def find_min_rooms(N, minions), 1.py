
def find_min_rooms(N, minions):
    ranges = []
    for minion in minions:
        ranges.append((minion[0], 1))
        ranges.append((minion[1] + 1, -1))

    ranges.sort()
    
    rooms = 0
    current_rooms = 0
    for range_val, change in ranges:
        current_rooms += change
        rooms = max(rooms, current_rooms)

    return rooms

# Input
N = int(input())
minions = []
for _ in range(N):
    L, U = map(int, input().split())
    minions.append((L, U))

# Output
result = find_min_rooms(N, minions)
print(result)
