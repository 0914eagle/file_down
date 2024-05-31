
def minimum_rooms_needed(N, preferences):
    intervals = []
    for pref in preferences:
        intervals.append((pref[0], pref[1]))
    
    intervals.sort()
    rooms = []
    for interval in intervals:
        assigned = False
        for room in rooms:
            if room[-1][1] < interval[0]:
                room.append(interval)
                assigned = True
                break
        if not assigned:
            rooms.append([interval])
    
    return len(rooms)

# Input
N = int(input())
preferences = []
for _ in range(N):
    pref = tuple(map(int, input().split()))
    preferences.append(pref)

# Output
print(minimum_rooms_needed(N, preferences))
