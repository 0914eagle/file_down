
def min_rooms_for_minions(N, minions):
    intervals = []
    for minion in minions:
        intervals.append((minion[0], 1))
        intervals.append((minion[1] + 1, -1))
    
    intervals.sort()
    
    rooms_needed = 0
    rooms_in_use = 0
    for interval in intervals:
        if interval[1] == 1:
            rooms_in_use += 1
            rooms_needed = max(rooms_needed, rooms_in_use)
        else:
            rooms_in_use -= 1
    
    return rooms_needed

# Input
N = int(input())
minions = []
for _ in range(N):
    L, U = map(int, input().split())
    minions.append((L, U))

# Output
print(min_rooms_for_minions(N, minions))
