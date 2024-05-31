
def min_rooms_for_minions(N, minions):
    intervals = []
    for minion in minions:
        intervals.append((minion[0], 1))
        intervals.append((minion[1] + 1, -1))
    
    intervals.sort()
    rooms_needed = 0
    curr_rooms = 0

    for interval in intervals:
        if interval[1] == 1:
            curr_rooms += 1
            rooms_needed = max(rooms_needed, curr_rooms)
        else:
            curr_rooms -= 1

    return rooms_needed

# Input parsing
N = int(input())
minions = []
for _ in range(N):
    L, U = map(int, input().split())
    minions.append((L, U))

# Calculate and output the minimum number of rooms needed
print(min_rooms_for_minions(N, minions))
