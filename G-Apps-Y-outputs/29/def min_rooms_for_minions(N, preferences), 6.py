
def min_rooms_for_minions(N, preferences):
    intervals = []
    for pref in preferences:
        intervals.append((pref[0], 1))  # Lower bound of interval
        intervals.append((pref[1] + 1, -1))  # Upper bound of interval + 1

    intervals.sort()
    
    rooms = 0
    current_rooms = 0
    for _, change in intervals:
        current_rooms += change
        rooms = max(rooms, current_rooms)

    return rooms

# Input
N = int(input())
preferences = []
for _ in range(N):
    L, U = map(int, input().split())
    preferences.append((L, U))

# Output
print(min_rooms_for_minions(N, preferences))
