
def minimum_rooms_needed(N, preferences):
    intervals = sorted(preferences, key=lambda x: x[0])
    rooms = []
    
    for interval in intervals:
        assigned = False
        for room in rooms:
            if interval[0] >= room[-1][1]:
                room.append(interval)
                assigned = True
                break
        if not assigned:
            rooms.append([interval])
    
    return len(rooms)

# Input processing
N = int(input())
preferences = []
for _ in range(N):
    L, U = map(int, input().split())
    preferences.append((L, U))

# Call the function and print the result
print(minimum_rooms_needed(N, preferences))
